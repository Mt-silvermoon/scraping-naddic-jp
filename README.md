scraping-naddic-jp
==================

[CLOSERSの公式サイトのニュース](https://closers.naddicjapan.com/news/)をスクレイピングして、Webhookに投げるスクリプト。

## Description
コマンドラインで起動させる常駐スクリプト。

疎通確認のため、初回起動時は最新の記事がすべてPOSTされるのでご注意ください。

デフォルトでは、5分置きにニュース情報を取得する。

更新頻度を変更する場合は、`scraping.py`のFREQUENCYの値を秒数単位で変更してください。

## Demo
![discord webhook demo](https://i.imgur.com/dbpnKME.jpg)

## Requirement
- Python3.x
- requests
- beautifulsoup4

## Install
```
python -m pip install requests bs4
```

## Usage
`scraping.py`のWEBHOOK_URLをPOST先のIncoming WebhookのURLに上書きして、実行する。

コマンドラインで起動し、常駐させておく。止める際はプロセスキルしてください。

```
python scraping.py
```
