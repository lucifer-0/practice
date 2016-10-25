# -*- coding:utf-8 -*-

import csv
import urllib
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


html = urllib.urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
page = html.read()
bs0bj = BeautifulSoup(page, 'html.parser')
table = bs0bj.findAll('table', {'class':'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('editors.csv', 'wt')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()