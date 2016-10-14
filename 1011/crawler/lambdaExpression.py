# -*- coding:utf-8 -*-

import re
import urllib
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/pages2.html'
html = urllib.urlopen(url)
page = html.read()
bs0bj = BeautifulSoup(page, 'html.parser')
tags = bs0bj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tags:
    print tag