# pip3 install requests
# pip3 install beautifulsoup4
# 작업을 할 때에는 가상환경을 잡고 그 안에서 라이브러리를 가지고 작업하는게 맞다.

import requests
from bs4 import BeautifulSoup

response = requests.get('https://ridibooks.com/category/2200')
response.encoding = 'utf-8'
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
l = []

for tag in soup.select('.title_text'):
    l.append(tag.text.strip())

print(l)

for i, j in enumerate(l, 1):
    print(i, j)