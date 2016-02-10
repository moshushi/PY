# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.weblancer.net/projects/"


def get_html(url):
    r = requests.get(url)
    return r.text

def parse(url):
    html = get_html(url)
    soup = BeautifulSoup(html)
    # return soup
    print soup.prettify().encode('UTF-8')



def main():
    # print(get_html(BASE_URL)).encode('utf-8')
    # print(parse(BASE_URL))
    parse(BASE_URL)


if __name__ == '__main__':
    main()
