# -*- coding:utf-8 -*-

import re
import urllib
from BeautifulSoup import BeautifulSoup

#page = urllib.urlopen('http://www.leeon.me')
#page = urllib.urlopen('http://www.meizitu.com')
html = urllib.urlopen('http://www.meizitu.com')
page = html.read()
#soup = BeautifulSoup(page, fromEncoding="gbk")
soup = BeautifulSoup(page, 'html.parser', fromEncoding='gbk')
images = soup.findAll('img', {'src':re.compile('.jpg')})

for image in images:
    print image['src']

#print soup.span


#print soup.originalEncoding
#print soup.prettify()

