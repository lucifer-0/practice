# -*- coding:utf-8 -*-

import os
import urllib
import urllib2
from bs4 import BeautifulSoup

html = urllib.urlopen('http://www.meizitu.com')

soup = BeautifulSoup(html, from_encoding='gbk')

print soup


'''
try:
    html = urllib.urlopen('http://caonima.com')
except urllib2.HTTPError as e:
    print e.reason
else:
    if html is None:
        print 'URL is not found'
    page = html.read()
    with open('data.txt', 'a+') as f:
        f.write(page)
'''





