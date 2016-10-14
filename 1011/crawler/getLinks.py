# -*- coding:utf-8 -*-

import re
import urllib
from bs4 import BeautifulSoup

def getLink(pageUrl):
    global pages
    html = urllib.urlopen('http://en.wikipedia.org' + pageUrl)
    soup = BeautifulSoup(html.read(), 'html.parser')

    try:
        print soup.h1.get_text()
        print soup.find(id = 'mw-content-text').findAll('p')[0]
        print soup.find(id = 'ca-edit').find('span').find('a').attrs['href']
    except AttributeError:
        print '页面缺少一些属性'

    bs0 = soup.findAll('a', href=re.compile('^(/wiki/)'))
    for link in bs0:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #遇到新页面
                newPage = link.attrs['href']
                print '---------', newPage
                pages.add(newPage)
                getLink(newPage)


if __name__ == '__main__':
    pages = set()
    getLink('')

