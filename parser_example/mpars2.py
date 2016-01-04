# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://freelance.ru"


def get_html(url):
    r = requests.get(url)
    return r.text


def parse(html):
    soup = BeautifulSoup(html)
    # table = soup.find('class', id="s_projects")
    # table = soup.find_all(attrs={"class": 'section', "id": 's_projects'})
    table = soup.find(class_='section', id='s_projects')
    rows = table.find_all(class_='proj public prio')
    pass
    # return rows
    print soup.prettify().encode('utf-8')

def out_console(res):
    return res.encode('utf-8')


def main():
    # print get_parse((get_html))
    # print out_console(get_html(BASE_URL))
    # get_parse(get_html(BASE_URL))
    # print parse(get_html(BASE_URL))
    parse(get_html(BASE_URL))
    pass

if __name__ == "__main__":
    main()
