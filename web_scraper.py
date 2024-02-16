"""Webスクレイピングツールテスト"""
# import packages
import urllib.request
from bs4 import BeautifulSoup

# the targeted URL
url = 'https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'

# use request to open the URL
ourUrl = urllib.request.urlopen(url)

soup = BeautifulSoup(ourUrl, 'html.parser')

print(soup.prettify())
