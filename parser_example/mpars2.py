# -*- coding: utf-8 -*-

"""
Source http://youtu.be/KPXPr-KS-qk
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://freelance.ru/projects/filter/'


def get_html(url):
    r = requests.get(url)
    return r.text


def parse(html):
    soup = BeautifulSoup(html)
    # print soup.prettify().encode('utf-8')
    table = soup.find(class_='projects')
    # print table.prettify().encode('utf-8')
    rows = table.find_all(class_='p_title')
    # print rows.prettify().encode('utf-8')
    for i in rows:
        print i.prettify().encode('utf-8')


def output_console(res):
    return res.encode('utf-8')


def main():
    # print output_console(get_html(BASE_URL))
    parse(get_html(BASE_URL))

if __name__ == '__main__':
    main()
