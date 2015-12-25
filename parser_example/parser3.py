# -*- coding: utf-8 -*-

"""
Вывод на печать r.text в кодировке консоли через изменение в r.encoding
для вывода в вим
"""

import requests

# BASE_URL = "http://www.jobs.ua/"
BASE_URL = "https://api.github.com/events"

def get_html():
    r = requests.get(BASE_URL)
    # r.encoding = 'UTF-8'
    output_console = r.text.encode('utf-8')
    print r.encoding
    return output_console

def main():
    print (get_html())


if __name__ == "__main__":
    main()
