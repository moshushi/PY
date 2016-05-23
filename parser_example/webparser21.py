# -*- encoding: utf-8 -*-
"""
Made in python 2.7.10
Script downloads and wraps projects from http://weblancer.net/
Script covered unittest =)
Source http://youtu.be/KPXPr-KS-qk
"""

import requests, csv
from bs4 import BeautifulSoup

# BASE_URL = "http://localhost/"
BASE_URL = "https://www.weblancer.net/jobs/"
NAME_COLUMM = ['Проект', 'Категори', 'Цена', 'Заявки']
PATH_FILE = 'proje.csv'

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
    print r.status
    return r.text

def get_html_count(html_doc):
    """
    Get pagination number
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    pagination = int(soup.find('ul', class_="pagination").findAll('li')[-1].
                     a['href'].lstrip('/jobs/?page='))
    return pagination

def parse(html_doc):
    """
    Parse current page and append result to list
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('div', class_="container-fluid cols_table show_visited")
#     print table.prettify().encode('UTF-8')
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
    html = get_html(url)
#     html = get_html_local()
    data = parse(html)
    return data

def parsing_all_page(url):
    """
    Parse all site uses page count
    """
    html_doc = get_html(url)
#     html_doc = get_html_local()
    page_count = get_html_count(html_doc)
    print 'All have find pages %d' % page_count

    projects = []

    for page in range(1, page_count + 1):
        print 'Parsing %d%%' % (page*100/page_count)

        url = BASE_URL + '?page=%d' % page
        projects.extend(process_page(url))

    return projects

def recode_for_write(sec):
    """
    Helper function for write dictonary values to windows code cp1251
    """
    sec2 = []
    for i in sec:
        sec2.append(i.decode('utf-8').encode('cp1251'))
#         sec2.append(i.encode('cp1251'))
    return sec2

def recode_value_dict(dictionary):
    """
    Recursively recode value in dictionary for write in windows code
    """
    somedict = {k:v.encode('cp1251') for k, v in dictionary.items()}
    return somedict

def save(projects, path):
    """
    Write projects to excel csv file
    """
    with open(path,'w') as csvfile:
#         writer = csv.writer(csvfile, delimiter=',', quotechar='"', lineterminator='\n')
        writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        # string for help MS Excel
        writer.writerow(["sep=,"])
        # Table name_columm
        writer.writerow(recode_for_write(NAME_COLUMM))

    with open(path,'a') as csvfile:
        headers = ['title', 'category', 'price', 'applications']
        writer = csv.DictWriter(csvfile, lineterminator='\n',
                                fieldnames=headers)
        for i in projects:
            i = recode_value_dict(i)
            writer.writerow(i)


def main():
#     data = process_page(BASE_URL)

#     data = parsing_all_page(BASE_URL)
#     save(data, PATH_FILE)

    get_html(BASE_URL)

if __name__ == '__main__':
    main()
