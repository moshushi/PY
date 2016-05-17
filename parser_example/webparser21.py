# -*- coding: utf-8 -*-

'''
Web-parse and save to export like Source: http://youtu.be/KPXPr-KS-qk
'''

import requests
from bs4 import BeautifulSoup

import os

BASE_URL = "https://www.weblancer.net/jobs/"
# BASE_URL = "https://www.weblancer.net/jobs/?type=project"
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'html.html')

def get_html_local():
    """
    Helper function for develop and unittest. Get html from local-pc
    """
    with open(TESTDATA_FILENAME, 'r') as html_file:
        testdata = html_file.read()
#     print testdata
    return testdata

def get_html(url):
    """
    Get html from website
    """
    r = requests.get(url)
    return r.text

def get_html_count(url):
    """
    Get pagination number
    """
    html_doc = get_html(url)
#     html_doc = get_html_local()
    soup = BeautifulSoup(html_doc, 'html.parser')
    pagination = int(soup.find('ul', class_="pagination").findAll('li')[-1]\
        .a['href'].lstrip('/jobs/?page='))
    return pagination


def main():
    pass
#     print get_html_count(BASE_URL)
#      print local_html()
#     print get_html(BASE_URL).encode('utf-8')
#     get_html_local()


if __name__=='__main__':
    main()
