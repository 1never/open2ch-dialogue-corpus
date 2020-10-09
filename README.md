# おーぷん2ちゃんねる対話コーパス
## 概要
[おーぷん2ちゃんねる](https://open2ch.net/)の「なんでも実況(ジュピター)」「ニュー速VIP」「ニュース速報+」の3つの掲示板をクロールして作成した対話コーパスです．
おーぷん2ちゃんねる開設時から2019年7月20日までのデータを使用して作成しました．

## 配布先
[こちら](https://drive.google.com/file/d/1-adMFRaJnzpVFf_NwsWU1s1a-NK4DoGZ/view?usp=sharing)からダウンロードしてください．
内容を見てみたい方のためのサンプルデータは[こちら](https://drive.google.com/file/d/1O24EfKI7Jsjvhh2Tq5qkCmyZP3b6bMnw/view?usp=sharing)．

## データ形式
* データはtsv形式であり，レスアンカー「>>」で指定された投稿同士をタブ区切りで連結しています．各行が1対話となります．

    例： [投稿1] [tab] [投稿2] [tab] [投稿3] ...

* 上の例では，投稿2は投稿1へのレスアンカーを(原文では)含み，投稿3は投稿2へのレスアンカーを(原文では)含んでいます．コーパス中ではレスアンカーは削除されています．
    * レスアンカーは文頭にあるもののみを使用し，文頭以外でレスアンカーを含む投稿は除外しています．
* 対話は2者が交互に投稿したもののみを収録しています．つまり，偶数番目の投稿と奇数番目の投稿はそれぞれ同じユーザが投稿したものです．
* 改行は「\_\_BR\_\_」という記号に置換されています．
* 以下の条件に該当する投稿は除外しています．
    * 文字数が5文字未満，および150文字より大きい投稿
    * URLおよび画像を含む投稿
    * 2つ以上のレスアンカーを含む投稿
    * ひらがな，カタカナ，漢字のいずれも含まない投稿
    * 4回以上の改行を含む投稿(対話としてふさわしくないもの，例えば打順や日程の列挙などを含むため)

### ファイル構成
| ファイル名 | 取得先 | 対話数 | 平均対話長 |
|-----------|-----------------------|-----------|-----------------------|
| livejupiter.tsv |なんでも実況(ジュピター) | 5948218 | 2.24 |
| news4vip.tsv | ニュー速VIP | 1983626 | 2.41 |
| newsplus.tsv | ニュース速報+ | 217296 | 2.09 |
|  | 合計| 8149140 | 2.28 |

## 前処理用スクリプト
様々な用途に利用しやすいよう，不適切な表現を含む投稿を除去するスクリプト(cleaning.py)と改行記号「\_\_BR\_\_」を句読点に置換するスクリプト(replace_br.py)を用意しました．両方のスクリプトを適用することで，不適切表現を除去し，かつ改行記号を句読点に変換することも可能です．
ただし，本スクリプトを適用しても，不適切な表現が完全に除去できるわけではありません．
また，読点とすべきところを句点とするなど，改行記号が正しく置換されない場合があります．

スクリプトはファイル単位で実行します．
livejupiter.tsvを対象にスクリプトを実行するコマンドは以下のとおりです．

### 不適切な用語の除去
```
$ python cleaning.py --input_file livejupiter.tsv --output_file livejupiter_cleaned.tsv
```
### 改行記号の置換
実行にはmecab-python3が必要です．
```
$ python replace_br.py --input_file livejupiter.tsv --output_file livejupiter_replaced.tsv
```

## 応答順位付けタスク用データ
文脈に対して複数の応答を順位付けするタスクに対応した開発データとテストデータを用意しています．
データの抽出元は同じく「なんでも実況(ジュピター)」「ニュー速VIP」「ニュース速報+」の3つの掲示板です．

開発データは2019年8月中に立てられたスレッドのみから，テストデータは同年9月中に立てられたスレッドのみからデータを構築しており，投稿の重複はありません．

### 配布先
[こちら](http://keldic.net/data/open2ch_dialogue_corpus_ranking.zip)からダウンロードしてください．

### データ形式
1つの文脈(コーパス本体における対話から，最後の投稿を除いたもの)につき，1つの実際の投稿と9つのランダムに抽出した投稿が収録されています．

データ形式はコーパス本体と同じtsv形式ですが，各行の先頭に，その行の最後の投稿が実際の投稿であるかランダム抽出の投稿であるかを意味するラベルが付与されています(1:実際の投稿，0:ランダム抽出)．

開発データ(dev.tsv)，テストデータ(test.tsv)にはそれぞれ2000個の文脈が収録されており，20000行ずつのファイルとなっています．

### 評価用スクリプト
応答順位付けタスクで評価尺度として用いられるRecall@k(k=1～10)を計算するスクリプトを用意しました．

開発データ(dev.tsv)，もしくはテストデータ(test.tsv)の各投稿に対するスコアのみが入った20000行のファイル(各行の数値が同じ行の投稿に対応)を用意し，以下のコマンドでスクリプトを実行できます．
```
$ python eval_ranking.py --input_file dev.tsv --score_file score_sample.txt
```

## 文献情報
本コーパスを使用した場合，以下を引用してください．
```
@inproceedings{open2chdlc2019,
  title={おーぷん2ちゃんねる対話コーパスを用いた用例ベース対話システム},
  author={稲葉 通将},
  booktitle={第87回言語・音声理解と対話処理研究会(第10回対話システムシンポジウム), 人工知能学会研究会資料 SIG-SLUD-B902-33},
  pages={129--132},
  year={2019}
}
```

