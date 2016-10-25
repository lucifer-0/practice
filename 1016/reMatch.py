# -*- coding:utf-8 -*-

import re


for i in range(2, 12):
    print i




'''



file = open('xscjcx.aspx', 'rb')
page = file.read()
file.close()
list = re.findall('<td>.*</td>{8,13}', page)
info = open('info9.txt', 'wb')
for item in list:
    info.write(item)
print list




file = open('xscjcx.aspx', 'rb')
page = file.read()
file.close()
list = re.findall('>(.*)<', page)
info = open('标签.txt', 'wb')
for item in list:
    info.write(item+'\n')
print list
'''


