#!/usr/bin/env python3
"""公開している登山口データの妥当性を確かめる（GitHub Actions と手元の両方で使う）。

  python3 scripts/validate_trailheads.py

エラーがあれば終了コード1。確認日が古い地点などは警告として出すだけで、失敗にはしない。
"""
import csv
import datetime
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TH = os.path.join(ROOT, "trailheads")
# 日本の範囲（南鳥島・与那国島まで含む）
LAT_RANGE = (20.0, 46.5)
LON_RANGE = (122.0, 154.5)
STALE_DAYS = 730                      # 公式情報の確認からこの日数が過ぎたら警告
CSV_COLUMNS = {"id", "kind", "name", "lat", "lon", "status", "sources"}

errors: list[str] = []
warnings: list[str] = []


def check_license() -> None:
    path = os.path.join(TH, "LICENSE.md")
    if not os.path.exists(path):
        errors.append("trailheads/LICENSE.md がない")
        return
    text = open(path, encoding="utf-8").read()
    for word in ("ODbL", "OpenStreetMap", "国土数値情報", "国土地理院"):
        if word not in text:
            errors.append(f"LICENSE.md に「{word}」の表示がない")


def check_json() -> None:
    path = os.path.join(TH, "trailheads.json")
    if not os.path.exists(path):
        errors.append("trailheads/trailheads.json がない")
        return
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:                               # noqa: BLE001
        errors.append(f"trailheads.json を読めない: {e}")
        return

    for key in ("version", "generatedAt", "attribution", "trailheads"):
        if key not in data:
            errors.append(f"trailheads.json に {key} がない")
    if errors:
        return

    if not any("OpenStreetMap" in a for a in data["attribution"]):
        errors.append("trailheads.json の attribution に OpenStreetMap の表示がない")
    try:
        datetime.date.fromisoformat(data["generatedAt"])
    except ValueError:
        errors.append(f"generatedAt の日付が不正: {data['generatedAt']}")

    points = data["trailheads"]
    if not points:
        errors.append("trailheads.json に地点が1つもない")
        return
    print(f"trailheads.json: {len(points)}地点 / 確認済み {sum(1 for p in points if p.get('verified'))} / "
          f"生成日 {data['generatedAt']}")

    seen: set[str] = set()
    today = datetime.date.today()
    stale = 0
    for p in points:
        pid = p.get("id")
        if not pid:
            errors.append("id のない地点がある")
            continue
        if pid in seen:
            errors.append(f"IDが重複している: {pid}")
        seen.add(pid)
        for key in ("name", "label", "lat", "lon", "verified", "mountainIds"):
            if key not in p:
                errors.append(f"{pid}: {key} がない")
        lat, lon = p.get("lat"), p.get("lon")
        if not (isinstance(lat, (int, float)) and LAT_RANGE[0] <= lat <= LAT_RANGE[1]):
            errors.append(f"{pid}: 緯度が日本の範囲外 ({lat})")
        if not (isinstance(lon, (int, float)) and LON_RANGE[0] <= lon <= LON_RANGE[1]):
            errors.append(f"{pid}: 経度が日本の範囲外 ({lon})")
        if p.get("verified"):
            basis = set(p.get("basis") or [])
            # 確認済みは「公式情報」または「OSM以外の情報源をもう1つ」で裏が取れていること
            if "official" not in basis and not (basis - {"osm"}):
                errors.append(f"{pid}: 確認済みなのに根拠がOSMだけ（basis={sorted(basis)}）")
            if "official" in basis and not p.get("officialUrls"):
                errors.append(f"{pid}: 公式情報で確認したことになっているが出典URLがない")
            checked = p.get("verifiedAt")
            if checked:
                try:
                    if (today - datetime.date.fromisoformat(checked)).days > STALE_DAYS:
                        stale += 1
                except ValueError:
                    errors.append(f"{pid}: verifiedAt の日付が不正 ({checked})")
    if stale:
        warnings.append(f"公式情報の確認から{STALE_DAYS}日以上たった地点が{stale}件ある。規制情報を確認し直すこと")


def check_csv() -> None:
    files = sorted(glob.glob(os.path.join(TH, "data", "*.csv")))
    if not files:
        errors.append("trailheads/data に CSV がない")
        return
    total = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            if not reader.fieldnames:
                errors.append(f"{os.path.basename(path)}: 見出し行がない")
                continue
            if "kind" not in reader.fieldnames:
                continue                                  # mountains.csv など地点以外のファイル
            missing = CSV_COLUMNS - set(reader.fieldnames)
            if missing:
                errors.append(f"{os.path.basename(path)}: 列が足りない {sorted(missing)}")
                continue
            rows = list(reader)
            total += len(rows)
            for row in rows:
                if row["status"] not in ("adopted", "provisional", "candidate"):
                    errors.append(f"{os.path.basename(path)}: status が不正 ({row['status']})")
                    break
                if not row["sources"]:
                    errors.append(f"{os.path.basename(path)}: {row['id']} に出典がない")
                    break
    print(f"地域別CSV: {len(files)}ファイル / {total}行")


check_license()
check_json()
check_csv()

for w in warnings:
    print(f"警告: {w}")
for e in errors:
    print(f"エラー: {e}")
print("検証: " + ("失敗" if errors else "OK"))
sys.exit(1 if errors else 0)
