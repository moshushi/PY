# -*- coding: utf-8 -*-

"""
Вывод на печать r.text в кодировке консоли через изменение в r.encoding
через питон запущенный из консоли
"""

import requests

# BASE_URL = "http://www.jobs.ua/"
BASE_URL = "https://api.github.com/events"

def get_html():
    r = requests.get(BASE_URL)
    r.encoding = 'cp866'
    return r.text
    # return r.content

def main():
    #r.encoding = 'cp866'
    print (get_html())


if __name__ == "__main__":
    main()
