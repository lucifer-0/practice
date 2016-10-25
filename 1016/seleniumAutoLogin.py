# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


#模拟登录教务系统
driver = webdriver.Chrome(executable_path='E:/Chrom/Chrome64_51.0.2704.84/chromedriver.exe')
driver.get('http://218.75.197.124:83/default2.aspx')
#用户名，密码，万恶的验证码
elem_user = driver.find_element_by_name('txtUserName')
elem_user.send_keys('15408500124')
elem_pwd = driver.find_element_by_name('TextBox2')
elem_pwd.send_keys('NC1284526746')
checkCode = raw_input('请输入验证码：')
elem_check = driver.find_element_by_name('txtSecretCode')
elem_check.send_keys(checkCode)
elem_check.send_keys(Keys.RETURN)




'''
reload(sys)
sys.setdefaultencoding('gb18030')
driver = webdriver.Firefox(executable_path='')
driver.get("http://www.baidu.com")
assert "百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.send_keys("Eastmount")
#elem.send_keys(Keys.RETURN)
assert "谷歌" in driver.title
driver.save_screenshot('baidu.png')
driver.close()
driver.quit()

'''
