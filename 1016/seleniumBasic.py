# -*- conding:utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.PhantomJS(executable_path='E:/code/python27/Lib/site-packages/phantomjs-2.0.0-windows/bin/phantomjs.exe')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print driver.find_element_by_id('content').text
driver.close()
