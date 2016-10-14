# -*- coding:utf-8 -*-

import re
import random
import urllib
import datetime
from bs4 import BeautifulSoup

def open_url(url):
    html = urllib.urlopen(url)
    page = html.read()
    return page

def getLink(url):
    link = []
    page = open_url(url)
    soup = BeautifulSoup(page, 'html.parser')
    for item in soup.findAll('a'):
        #if 'href' in item.attrs:
           # print item.attrs['href']
        print item

def getLinks(articleUrl):
    html = open_url('http://en.wikipedia.org' + articleUrl)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))

if __name__ == '__main__':
    '''
    url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
    getLink(url)
    '''
    random.seed(datetime.datetime.now())

    links = getLinks('/wiki/Kevin_Bacon')

    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print newArticle
        links = getLinks(newArticle)



