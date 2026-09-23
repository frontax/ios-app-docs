# 登山口データ（Trailhead data）

iOSアプリ「登山記録」で使っている、日本の名山の**登山口・駐車場・バス停**のデータです。
OpenStreetMap の派生データベースにあたるため、[Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/) で公開します。

- 最終更新: **2026-09-23**
- 登山口 3,179地点（うち公式情報で確認済み 416地点）、駐車場 1,641地点、バス停 1,991地点
- 対象の山 929座（日本百名山・二百名山・三百名山の301座と、地域の百名山628座）

## 出典の表示

このデータを利用する場合は、次の表示が必要です。

- **© OpenStreetMap contributors** — [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/)
- **「国土数値情報（バス停留所データ）」（国土交通省）を加工して作成** — バス停の位置・名称
- **出典：国土地理院** — 地名検索および地理院地図（ベクトルタイル提供実験）による位置の照合

詳しい条件は [LICENSE.md](LICENSE.md) を参照してください。

## ファイル

| ファイル | 内容 |
| --- | --- |
| [trailheads.json](trailheads.json) | アプリが使う形式。確認済みを中心とした登山口と、その周辺の駐車場・バス停 |
| [data/summary.md](data/summary.md) | 地域別の収集状況 |
| [data/mountains.csv](data/mountains.csv) | 対象の山の一覧（山名・標高・所在地・リスト区分） |
| `data/<地域>.csv` | 地域別の全地点（登山口・駐車場・バス停）。北海道・東北・関東・甲信越・北陸・東海・関西・中国・四国・九州 |
| `data/<地域>.geojson` | 同じ内容の GeoJSON |
| [data/source_audit.csv](data/source_audit.csv) | 地点ごとの出典の内訳 |

## trailheads.json の構造

```jsonc
{
  "version": 1,
  "generatedAt": "2026-09-23",
  "osmData": "japan-latest.osm.pbf 2026-09-18T20:21:10Z",
  "attribution": ["© OpenStreetMap contributors (ODbL 1.0)", "..."],
  "trailheads": [
    {
      "id": "TH-n1280146188",      // 地点ID（OSMの要素、または国土地理院の照合による地点）
      "name": "利尻北麓野営場（鴛泊コース登山口）",  // 正式な名称
      "label": "利尻北麓野営場",      // 地図のラベル用の短い名前
      "lat": 45.22279, "lon": 141.21253,  // WGS84 十進法
      "verified": true,             // 公式情報、または独立した2情報源で確認済みか
      "mountainIds": [2],           // mountains.csv の mountainId
      "basis": ["official"],        // 確認の根拠 official / gsiName / gsiTrail / ksj / osm
      "verifiedAt": "2026-09-20",   // 公式情報を確認した日
      "attrs": [ { "key": "parking", "text": "..." } ],  // 規制・駐車場・季節閉鎖など
      "notes": ["..."],             // 利用上の注意
      "officialUrls": ["https://..."],
      "parking": [ ... ], "busStops": [ ... ]
    }
  ]
}
```

## 地域別CSVの `status`

| 値 | 意味 |
| --- | --- |
| `adopted` | 公式情報（自治体・都道府県・環境省・林野庁・管理者・交通事業者）、または独立した2情報源で名称・位置を確認した |
| `provisional` | OSM由来の名称などから登山口とみられるが、公式情報では未確認 |
| `candidate` | 登山道が道路と接する地点として機械的に抽出した候補。名称も未確認 |

`trailheads.json` の `verified` は `adopted` に対応します。

## 作り方

1. OpenStreetMap の日本全域データ（Geofabrik の `japan-latest.osm.pbf`）から、山頂の周囲22kmにある登山道・道路・駐車場・バス停・山小屋などを抽出
2. 登山道が車道と接する地点を登山口の候補とし、名称・林道のゲート・山頂までの距離などで絞り込み
3. 自治体・都道府県・環境省・林野庁・管理者・交通事業者の公式情報で名称と位置を確認。位置は国土地理院の地名検索・標高API・地理院地図（徒歩道が車道から始まる位置）と照合
4. 確認した内容と出典URLを地点ごとに記録

Overpass API は使わず、OSMのデータはローカルのPBFからのみ抽出しています。民間の登山情報サイトの座標は使用していません。

## 注意

- **規制・通行止め・季節閉鎖の情報は `verifiedAt` の時点のものです。** 入山前に、各自治体・管理者・気象庁の最新情報を必ず確認してください
- `verified` が false の地点は公式情報で確認していません。位置が実際の登山口とずれている場合があります
- 登山口までの道路の通行可否、駐車場の利用可否は変わります。このデータは通行や安全を保証するものではありません
