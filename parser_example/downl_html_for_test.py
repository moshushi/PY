# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.weblancer.net/jobs/"

r = requests.get(BASE_URL)
html = r.text
html_w = r.text.encode('utf-8')

# soup = BeautifulSoup(html, 'html')

f = open('html.html', 'wb')
f.write(html_w)

# f = open('soup.html', 'w')
# f.write(soup)

f.close
