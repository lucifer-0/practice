# -*- coding:utf-8 -*-

import os
import urllib
from bs4 import BeautifulSoup


downloadDirectory = "download"
baseUrl = 'http://pythonscraping.com'


def getAbsoluteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http;//' + source
    else:
        url = baseUrl + '/' + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.mkdir(directory)
    return path


url = 'http://www.pythonscraping.com'
html = urllib.urlopen(url)
page = html.read()
bs0bj = BeautifulSoup(page, 'html.parser')
#imageLocation = bs0bj.find('a', {'id':'logo'}).find('img')['src']
#urllib.urlretrieve(imageLocation, 'logo.jpg')
downList = bs0bj.findAll(src=True)

for download in downList:
    fileUrl = getAbsoluteURL(baseUrl, download)
    if fileUrl is not None:
        print fileUrl

urllib.urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))






