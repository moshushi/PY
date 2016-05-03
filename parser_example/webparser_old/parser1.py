# -*- coding: utf-8 -*-

import requests

"""
Просмотр через r.content
"""

# BASE_URL = "http://www.jobs.ua/"
BASE_URL = "https://api.github.com/events"

def get_html():
    r = requests.get(BASE_URL)
    return r.content

def main():
    print (get_html())


if __name__ == "__main__":
    main()
