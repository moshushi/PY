# -*- coding: utf-8 -*-

"""
Source http://youtu.be/KPXPr-KS-qk
"""

import requests
from bs4 import BeautifulSoup
import collections

BASE_URL = 'https://freelance.ru/projects/filter/'


def get_html(url):
    r = requests.get(url)
    return r.text


def parse(html):
    soup = BeautifulSoup(html)
    # print soup.prettify().encode('utf-8')
    table = soup.find(class_='projects')
    # print table.prettify().encode('utf-8')
    # rows = table.find_all(class_='p_title')
    # for i in rows:
    #     print i.prettify().encode('utf-8')

    projects = []

    for row in table.find_all(class_='p_title'):
        bol = row.find(class_='ptitle').span
        print bol
        print 'hhh'
        col = row.find('span')
        print col
        cols = row.find_all('span')
        print cols
        # print type(cols)
        projects.append({
            'title': cols[0]
        })

   #  for project in projects:
   #      print project

def output_console(res):
    return res.encode('utf-8')



def main():
    # print output_console(get_html(BASE_URL))
    parse(get_html(BASE_URL))

if __name__ == '__main__':
    main()
