# -*- coding: utf-8 -*-

'''
Web-parse and save to export like Source: http://youtu.be/KPXPr-KS-qk
'''

import requests
from bs4 import BeautifulSoup

import os

BASE_URL = "http://localhost/"
# BASE_URL = "https://www.weblancer.net/jobs/"
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

def parse(url):
    """
    Parse current page and append result to list
    """
#     html_doc = get_html(url)
    html_doc = get_html_local()
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('div', class_="container-fluid cols_table show_visited")

    jobstats = []

    for row in table:
        jobstats.append({
            "title":row.find('div', class_="col-sm-7").a.text,
            "category":row.find('div', class_="text-muted").a.text,
            "price":row.find('div', class_="col-sm-2 amount title").text.strip(),
            "applications":row.find('div', class_="col-sm-3 text-right text-nowrap hidden-xs").text.strip()
        })


    return jobstats


def main():
    pass
#     print parse(BASE_URL)


if __name__=='__main__':
    main()
