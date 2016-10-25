# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp//mysql.sock', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute('USE scraping')

cur.execute('SELECT * from pages WHRER id = 1')
print cur.fetchone()
cur.close()
conn.close()
