# -*- coding: utf-8 -*-

'''
Web-parse and save to ecport like Source: http://youtu.be/KPXPr-KS-qk
'''

import requests

BASE_URL = "https://www.weblancer.net/projects/"

def get_html(url):
    r = requests.get(url)
    return r
