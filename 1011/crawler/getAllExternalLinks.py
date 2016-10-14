# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urlparse import urlparse
import re
import datetime
import random
import urllib


pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc
    internalLinks = []
    # Finds all links that begin with a '/'
    for link in bsObj.findAll('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with 'http' or 'www' that do
    # not contain the current URL
    for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts


def getRandomExternalLink(startingPage):
    html = urllib.urlopen(startingPage)
    bsObj = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print 'No external links, looking around the site for one'
        domain = urlparse(startingPage).scheme+'://'+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return internalLinks[random.randint(0, len(internalLinks) - 1)]
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink('http://oreilly.com')
    print 'Random external link is: %s' % externalLink
    followExternalOnly(externalLink)


#Collects a list of external URLs found in site
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urllib.urlopen(siteUrl)
    bs0bj = BeautifulSoup(html, "html.parser")
    domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
    internalLinks = getInternalLinks(bs0bj, domain)
    externalLinks = getExternalLinks(bs0bj, domain)
    for link in externalLinks:
        if link not in externalLinks:
            allExtLinks.add(link)
    for link in internalLinks:
        if link  not in allIntLinks:
            print 'next link is: %s' % link
            allIntLinks.add(link)
            getAllExternalLinks(link)


url1 = "http://oreilly.com"
url2 = "http://www.meizitu.com"
#followExternalOnly('http://oreilly.com')
#followExternalOnly('http://www.meizitu.com')

allIntLinks.add(url2)
getAllExternalLinks(url2)
for link in allExtLinks:
    print link, "++++++++++++++"

for link in allIntLinks:
    print link, "--------------"