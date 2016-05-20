# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://localhost/"
# BASE_URL = "https://www.weblancer.net/jobs/"

def get_html_local():
    """
    Helper function for develop and unittest. Get html from local-pc
    """
    import os
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'html.html')
    with open(TESTDATA_FILENAME, 'r') as html_file:
        testdata = html_file.read()
    return testdata

def get_html(url):
    """
    Get html from website
    """
    r = requests.get(url)
    return r.text

def get_html_count(html_doc):
    """
    Get pagination number
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    pagination = int(soup.find('ul', class_="pagination").findAll('li')[-1].a['href'].lstrip('/jobs/?page='))
    return pagination

def parse(html_doc):
    """
    Parse current page and append result to list
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('div', class_="container-fluid cols_table show_visited")
#    print table.prettify().encode('UTF-8')
    jobstats = []

    for row in table:
        jobstats.append({
            "title":row.find('div', class_="col-sm-7").a.text,
            "category":row.find('div', class_="text-muted").a.text,
            "price":row.find('div', class_="col-sm-2 amount title").text.strip(),
            "applications":row.find('div', class_="col-sm-3 text-right text-nowrap hidden-xs").text.strip()
        })
    return jobstats


def process_page(url):
    """
    Processing page
    """
#     html = get_html(url)
    html = get_html_local()
    data = parse(html)
    return data

def parsing_all_page(url):
    """
    Parse all site uses page count
    """
#     html_doc = get_html(url)
    html_doc = get_html_local()
    page_count = get_html_count(html_doc)
    print 'All have find pages %d' % page_count

    projects = []

    for page in range(1, page_count):
        print 'Parsing %d%%' % (page*100/page_count)

        url = BASE_URL + '?page=%d' % page
        projects.extend(process_page(url))

    return projects


def main():
#     dar = process_page(BASE_URL)
    dar = parsing_all_page(BASE_URL)
    loc = dar[2]
    print loc
    print loc["title"]
    print loc["category"]
    print loc["price"]
    print loc["applications"]
    print dar[2]["price"]

if __name__ == '__main__':
    main()
