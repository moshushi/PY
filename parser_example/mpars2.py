# -*- coding: utf-8 -*-

"""
Source http://youtu.be/KPXPr-KS-qk
http://wiki.python.su/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8/BeautifulSoup
http://wiki.python.su/Документации/BeautifulSoup
http://wiki.python.su/Beautiful_Soup/3.1.0

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
        bols = row.find(class_='ptitle').span.renderContents()
        print bols

        # prices = row.find_all(class_='hidden-xs')
        prices = row.find_all('b')
        print prices

        ## work with pymode out, not in python-shell
        # for line in prices:
        #     # print line.__str__()
        #     print line.renderContents()

        ## work with pymode out, not in python-shell
        # for line in prices:
        #     print line.encode('utf-8')

        # print unicode.join(u'\n',map(unicode,prices))

        projects.append({
            'title': bols,
            'price': prices
        })

    for project in projects:
        # print project
        pass

def output_console(res):
    return res.encode('utf-8')



def main():
    # print output_console(get_html(BASE_URL))
    parse(get_html(BASE_URL))

if __name__ == '__main__':
    main()
