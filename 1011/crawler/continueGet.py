# -*- coding:utf-8 -*-

import re
import sys
import urllib
import random
import datetime
from bs4 import BeautifulSoup

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    pass

def getAllInternalLinks(siteUrl):
    pass

#获取页面所有内链的列表
def getInternalLinks(bs0bj, includeUrl):
    internalLinks = []
    for link in bs0bj.findAll('a', href = re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面所有外链的列表
def getExternalLinks(bs0bj, excludeUrl):
    excludeLinks = []
    for link in bs0bj.findAll('a', href = re.compile('^(http://|www)((?!'+ excludeUrl +').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in excludeLinks:
                excludeLinks.append(link.attrs['href'])
    return excludeLinks

def getRandomExternalLinks(staringPage):
    html = urllib.urlopen(staringPage)
    bs0bj = BeautifulSoup(html.read(), 'html.parser')
    externalLinks = getExternalLinks(bs0bj, splitAddress(staringPage))
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(staringPage)
        if len(internalLinks) == 0:
            print '该页面没有内链了,程序终止'
            return None
        else:
            internalLink = internalLinks[random.randint(0, len(internalLinks)-1)]
            print '随机内链是： %s' % internalLink
            return internalLink
    else:
        externalLink = externalLinks[random.randint(0, len(externalLinks)-1)]
        print '随机外链是： %s' % externalLink
        return externalLink

def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')[0]
    return addressParts

def followExternalOnly(staringSite):
    externalLink = getRandomExternalLinks(staringSite)
    followExternalOnly(externalLink)


if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    followExternalOnly('http://www.meizitu.com')