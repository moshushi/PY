# -*- coding: utf-8 -*-
"""
Made in python 2.7.10
Source http://youtu.be/KPXPr-KS-qk
On new site
"""

import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.weblancer.net/projects/"
# NAME_COLUMM = ['Проект', 'Категори', 'Цена', 'Заявки']
NAME_COLUMM = ['Проект', 'Категори', 'Цена', 'Заявки']
PATH_FILE = 'proje.csv'


def get_html(url):
    """
    Get html page
    """
    r = requests.get(url)
    return r.text

def get_page_count(html):
    """
    Count page for parsing
    """
    soup = BeautifulSoup(html)
    paggination = int(soup.find('ul', class_="pagination").findAll('li')[-1].a['href'].lstrip('/projects/?page='))
    return paggination

def RecodeFoWrite(sec):
    """
    Helper function for write utf-8 to windows code cp1251
    """
    sec2 = []
    for i in sec:
        sec2.append(i.decode('utf-8').encode('cp1251'))
    return sec2

def RecodeFoWriteOnlyCP(sec):
    """
    Helper function for write dictionary values to windows code cp1251
    """
    sec2 = []
    for i in sec:
        sec2.append(i.encode('cp1251'))
    return sec2

def save(projects, path):
    """
    Helper function save result to file
    """
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['sep=,'])
        # String for help MS Excel right format open file
        writer.writerow(RecodeFoWrite(NAME_COLUMM))

        for project in projects:
            project_list = []
            for i in (project['title'], project['category'], project['price'], project['applications']):
                project_list.append(i)

            writer.writerow(RecodeFoWriteOnlyCP(project_list))

def parse(url):
    """
    Parse current page and append result to list
    """
    html = get_html(url)
    soup = BeautifulSoup(html)
    # return soup
#     print soup.prettify().encode('UTF-8')


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



def main():
    page_count = get_page_count(get_html(BASE_URL))

#     print 'Всего найденно страниц %d' % page_count
    print 'All have find pages %d' % page_count

    projects = []

#     print 'len is %d' % len(projects)

    for page in range(1, page_count):
#     for page in range(1, 3):
#         print 'Парсинг %d%%' % (page*100/page_count)
        print 'Parsing %d%%' % (page*100/page_count)
        projects.extend(parse(BASE_URL + '?page=%d' % page))
#         print 'len is %d' % len(projects)

    save(projects, PATH_FILE)

#     for project in projects:
#         print project


if __name__ == '__main__':
    main()
