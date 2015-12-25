# -*- coding: utf-8 -*-

"""
просмотр дополнительных параметров
"""

import requests

# BASE_URL = "http://www.jobs.ua/"
BASE_URL = "https://api.github.com/events"

def get_html():
    r = requests.get(BASE_URL)
    for i in dir(r):
        print i
    print dir(r)

def main():
    print (get_html())


if __name__ == "__main__":
    main()
