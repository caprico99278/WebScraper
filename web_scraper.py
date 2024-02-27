"""Webスクレイピングツールプロトタイプ"""

# パッケージのインポート
import requests
from bs4 import BeautifulSoup

# スクレイピング対象のサイトのURL
url = 'https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'

# サイトを開いて、開いたページのHTMLを取得
ourUrl = requests.get(url, timeout=60)

# 文字化け防止
ourUrl.encoding = ourUrl.apparent_encoding

# Webスクレイピング用オブジェクトへ変換
soup = BeautifulSoup(ourUrl.text, 'html.parser')

# 変換結果をファイルに書き出す
with open('myfile.txt', mode='w', encoding='utf-8') as f:
    items = []
    html_item_cards = soup.select('[data-testid="menu-item-tag"]')

    for html_item_card in html_item_cards:

        # TODO:抜き出すべきタグとテキスト情報の選定
        item = {}
        items.append(item)
        f.write(html_item_card.get_text() + '\n')
