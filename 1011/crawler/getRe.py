# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import re
import os

#url = 'http://tieba.baidu.com/p/3821063931'
url = 'http://www.meizitu.com'

def open_url(url):
    html = urllib.urlopen(url)
    page = html.read()
    return page

def parse(page):
    images = []
    soup = BeautifulSoup(page, 'html.parser', from_encoding='gbk')
    list = soup.findAll('img', {'src':re.compile('.jpg')})
    for image in list:
        images.append(image['src'])
    return images

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    os.chdir(path)

def getImg(images):
    for image in images:
        filename = image.split('/')[-1]
        with open(filename, 'wb') as f:
            img = urllib.urlopen(image)
            f.write(img.read())

if __name__ == '__main__':
    page = open_url(url)
    images = parse(page)
    mkdir('mm')
    getImg(images)




