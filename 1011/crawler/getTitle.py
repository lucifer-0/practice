# -*- coding:utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urllib.urlopen(url)
    except urllib2.HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read(), 'html.parser', from_encoding='gbk')
        title = soup.title
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.leeon.me')
if title == None:
    print 'Title could not be found'
else:
    print title

