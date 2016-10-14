# -*- coding:utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup

url = 'http://www.leeon.me'

html = urllib.urlopen(url)

page = html.read()

soup = BeautifulSoup(page, 'html.parser', from_encoding='gbk')

greenList = soup.findAll('span', {'class':'mon'})

for item in greenList:
    print item




