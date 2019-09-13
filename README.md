# おーぷん2ちゃんねる対話コーパス
## 概要
[おーぷん2ちゃんねる](https://open2ch.net/)の「なんでも実況(ジュピター)」「ニュー速VIP」「ニュース速報+」の3つの掲示板をクロールして作成した対話コーパスです．
使用したデータはおーぷん2ちゃんねる開設時から2019年7月20日までのデータです．

## 配布先
[こちら](http://keldic.net/data/open2ch_dialogue_corpus.zip)からダウンロードしてください．
内容を見てみたい方のためのサンプルデータは[こちら](http://keldic.net/data/corpus_sample.tsv)．

## データ形式
* データはtsv形式であり，レスアンカー「>>」で指定された投稿同士をタブ区切りで連結しています．各行が1対話となります．

    例： [投稿1] [tab] [投稿2] [tab] [投稿3] ...

* 上の例では，投稿2は投稿1へのレスアンカーを(原文では)含み，投稿3は投稿2のレスアンカーを(原文では)含んでいます．
ただし，コーパス中ではレスアンカーは除外されています．
    * 2つ以上のレスアンカーを含む投稿は除外しています．
* 対話は2者が交互に投稿したもののみを収録しています．つまり，偶数番目の投稿と奇数番目の投稿はそれぞれ同じユーザが投稿したものです．
* 文字数が5文字未満，および150文字より大きい投稿は除外しています．
* 改行は「\_\_BR\_\_」という記号に置換されています．

### ファイル構成
| ファイル名 | 取得先 | 対話数 | 平均対話長 |
|-----------|-----------------------|-----------|-----------------------|
| livejupiter.tsv |なんでも実況(ジュピター) | 5948218 | 2.24 |
| news4vip.tsv | ニュー速VIP | 1983626 | 2.41 |
| newsplus.tsv | ニュース速報+ | 217296 | 2.09 |
|  | 合計| 8149140 | 2.28 |
