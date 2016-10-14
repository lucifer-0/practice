# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re
import datetime
import random
import urllib
from urlparse import urlparse

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
        if len(internalLinks) == 0:
            print 'No internal links'
            return None
        else:
            internalLink = internalLinks[random.randint(0, len(internalLinks) - 1)]
            print 'Random internal link is: %s' % internalLink
            return internalLink
    else:
        externalLink = externalLinks[random.randint(0, len(externalLinks) - 1)]
        print 'Random external link is: %s' % externalLink
        return externalLink


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink('http://oreilly.com')
    if externalLink is not None:
        followExternalOnly(externalLink)
    else:
        print 'This program is over'


#followExternalOnly('http://oreilly.com')
followExternalOnly('http://www.meizitu.com')