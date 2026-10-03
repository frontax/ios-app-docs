# 登山口データの出典とライセンス

このディレクトリのデータ（登山口・駐車場・バス停）は、次の情報源から作成しています。地点ごとの出典は、地域別CSVの `sources` 列にあります。

**このデータ全体は [Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/) で提供します。** 利用・再配布の際は、下の「出典の表示」に挙げた表示を行い、派生物も同じライセンスで提供してください。

## OpenStreetMap（主要な情報源）
- **表示**: © OpenStreetMap contributors
- **ライセンス**: [Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/)
- **取得元**: [Geofabrik](https://download.geofabrik.de/asia/japan.html) の日本全域データ（`japan-latest.osm.pbf`）。データの時点は各行の `sources` に記載
- **扱い**: このデータはOSMの**派生データベース**にあたります。**公開・配布する場合は ODbL で提供し、出典を表示する必要があります**（下の「配布するときの条件」を参照）

## 国土地理院（地名の照合）
- **表示**: 出典：国土地理院
- **内容**: 地理院地図の地名検索の結果と、候補の位置が一致するかの確認に使用。一致した地名と元の座標（JGD2011）を `sources` に記録
- **内容（地理院地図のベクトルタイル）**: [国土地理院ベクトルタイル（試験公開）](https://github.com/gsi-cyberjapan/gsimaps-vector-experiment)の道路中心線のうち徒歩道（ftCode 2721）が車道から始まる位置を、登山口の位置の照合に使用。一致した位置（JGD2011）を `sources` に記録（地図データそのものは配布しない）。出典の表示は「国土地理院ベクトルタイル提供実験」
- **条件**: [国土地理院コンテンツ利用規約](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)（PDL1.0）。地名検索は主に地理院地図からの利用を想定した機能で、仕様は予告なく変わり得る（[国土地理院の回答](https://github.com/gsi-cyberjapan/gsimaps/issues/29)）

## 国土数値情報（バス停）
- **表示**: 「国土数値情報（バス停留所データ）」（国土交通省）を加工して作成
- **取得元**: [バス停留所データ 令和4年度](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P11-v3_0.html)（令和4年8月時点、JGD2011）
- **条件**: [国土数値情報ダウンロードサイトコンテンツ利用規約](https://nlftp.mlit.go.jp/ksj/other/agreement_01.html)。商用利用可、CC BY 4.0 と互換。加工したことを明示し、国が作成したかのような表示はしない

## 名山リスト
- 日本百名山・二百名山・三百名山の所属は、[日本山岳会の山岳リスト](https://jac1.or.jp/wp-content/uploads/2016/10/300meizanlist%E3%80%80.pdf)と日本語版Wikipediaの一覧で照合（事実のみ参照。本文は転載していない）
- 地域の百名山は、アプリ同梱の `famous_mountains.json` の区分を使用（原典との照合は未了）

## 使っていない情報源
- 山と溪谷オンライン等の民間の登山情報サイトの座標は**使用していません**。百名山の既存データ（`RouteData`）のうち、これらのサイト由来の座標は照合にも使わず、名称の照合だけに使っています

## 座標について
- すべて **WGS84の十進法**。国土地理院・国土数値情報由来の値は JGD2011 で、WGS84とは1m未満の差のため同一として扱い、元の値を `sources` に記録しています

## 出典の表示

- **© OpenStreetMap contributors**（ODbL 1.0）
- **「国土数値情報（バス停留所データ）」（国土交通省）を加工して作成**
- **出典：国土地理院**

## 配布するときの条件
1. **ODbL の継承**: OSM由来の座標を含むこのデータを配布する場合は、**同じデータを ODbL で公開**する必要があります。アプリ「登山記録」が使っているデータは、このディレクトリで公開しています
2. **アプリ内の出典表示**: 「© OpenStreetMap contributors」に加え、バス停の公式データを載せる場合は「国土数値情報（バス停留所データ）（国土交通省）」、地名の照合結果を載せる場合は「出典：国土地理院」を表示します
3. **検証状態の明示**: `status` が `provisional` / `candidate` の地点は未確認です。利用者に位置の確からしさが伝わる表示にします
