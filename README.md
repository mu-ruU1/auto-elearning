# e-learning の自動化ツール

## 概要

e-learning のポイントを自動で貯めてくれるツールを作ってみました。  
selenium という Web ブラウザの操作を自動化するためのフレームワークを使い、ログインからすべて自動で動作します。

## 動作環境

- Google Chrome ただしバージョンは問わない

## インストール

1. コマンドプロンプトにて pip のアップデート

```bash
pip install --upgrade pip
```

2. Python を[インストール](https://www.python.jp/install/windows/install.html)

3. selenium Python のインストール

```bash
pip install selenium
```

4. ChromeDriver の[インストール](https://www.seleniumqref.com//introduction/java/Java_Dl2.html)
   - ChromeDriver はお使いの Chrome のバージョンと一致したバージョンを使用してください。

## 準備

- 同じディレクトリ内に `library.py` というファイルを作成してください。  
  ファイルの中は以下のようにしてください。

- `trynum`の数値を変えることによって付与される pts が変わります。  
  <br>

```bash
#ID
myid = "ここにIDを挿入"

#パスワード
mypw = "ここにパスワードを挿入"

#chrome driverのフルパスを指定
chromedriver = "例）C:/chromedriver_win32/chromedriver.exe"

#e-learningログイン画面のURL
URL = "ここにURLを挿入"

#繰り返しの回数（この場合４回繰り返され、４０ptsが付与されます）
trynum = 4
```

## 使い方

次に示すファイルを実行することで動作します

`elearning.py`  
実際に画面に表示され、正常に動作しているか確認することができます
<br>
<br>

`elearning-headless.py`  
コンソールのみが開かれ、バックグラウンドで動作します
