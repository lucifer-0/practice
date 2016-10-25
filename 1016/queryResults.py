# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pytesser
import urllib
import urllib2
import cookielib
import time
import robotparser



class ResultSpider:
    def __init__(self):
        self.credit = []
        self.driver = webdriver.Chrome(executable_path='E:/Chrom/Chrome64_51.0.2704.84/chromedriver.exe')


    def crack(self):
        #img = self.driver.find_element_by_id('icode').get_attribute('src')
        # img = self.driver.get("http://218.75.197.124:83/CheckCode.aspx").read()
        #url = 'http://218.75.197.124:83/CheckCode.aspx'
        #img = urllib.urlopen(url).read()
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        img = self.driver.find_element_by_id('icode')
        ActionChains(self.driver).context_click(self.driver.find_element_by_id('icode'))
        ActionChains(self.driver).move_by_offset(5, 10)
        with open('CheckImage.gif', 'wb') as f:
            f.write(img)
        img = Image.open('CheckImage.gif')
        im = img.convert("L")
        im2 = Image.new("L", im.size, 255)
        for x in range(im.size[1]):
            for y in range(im.size[0]):
                pix = im.getpixel((y, x))
                if pix == 17:  # these are the numbers to get
                    im2.putpixel((y, x), 0)
        text = pytesser.image_to_string(im2)
        return text

    def login(self, username, password):
        login_if = False

        while not login_if:
            try:
                #访问教务系统网站
                self.driver.get('http://218.75.197.124:83/default2.aspx')
                #ActionChains(self.driver).move_to_element(img)
                reset = self.driver.find_element_by_name('Button2').click()
                checkCode = self.crack()
                #用户名，密码， 万恶的验证码
                self.driver.find_element_by_name('txtUserName').send_keys(username)
                self.driver.find_element_by_name('TextBox2').send_keys(password)
                #checkCode = raw_input('请输入验证码：')
                elem_check = self.driver.find_element_by_name('txtSecretCode').send_keys(checkCode)
                login_in = self.driver.find_element_by_name('Button1').click()
                #elem_if = self.driver.find_element_by_tag_name('title')
                if self.driver.title.encode(encoding='utf-8') == '正方教务管理系统':
                    login_if = True
                    print '登录成功'
                    break
            except UnexpectedAlertPresentException, NoSuchElementException:
                alert = self.driver.switch_to_alert()
                print alert.text
                alert.dismiss()



    def choose(self, id, value):
        sel = self.driver.find_element_by_xpath('//select[@id='+id+']')
        Select(sel).select_by_value(value)


    def activeInfo(self):
        #select = Select(self.driver.find_element_by_class_name("down"))  # 直接套用不需要修改
        #select.select_by_visible_text("信息查询")  # 通过显示的文字来选择
        elem_dw = ''
        try:
            #select = self.driver.find_element_by_xpath("//li[@class='top'][6]").click()
            #elem_onlineClass = self.driver.find_element_by_xpath("//ul[@class='nav']/li[2]").click()
            # elem_back = self.driver.find_element_by_xpath("//ul[@class='nav']/li[6]").click()
            # elem_temp = self.driver.find_element_by_xpath("//p[@class='location']").click()
            # select_year = self.driver.find_element_by_xpath("//select[@id='ddlXN']").click()
            # select_year = self.driver.find_element_by_class_name('search_con').click()
            # ActionChains(self.driver).move_by_offset(xoffset=50, yoffset=0).perform()
            # ActionChains(self.driver).move_to_element('ddlXN').perform()
            # time.sleep(3)
            # elem_searchbox = self.driver.find_element_by_xpath("//div[@class='searchbox']")
            # elem_queryInfo = self.driver.find_element_by_xpath("//ul[@class='nav']/li[6]").click()
            # elem_resultQuery = self.driver.find_element_by_xpath("//ul[@class='sub']/li[3]").click()
            # time.sleep(3)
            # self.driver.find_element_by_xpath("//span[@class='formbox']")

            #定位恶心的悬停下拉框, xpath大法好
            elem_queryInfo = self.driver.find_element_by_xpath("//ul[@class='nav']/li[6]").click()
            elem_resultQuery = self.driver.find_element_by_xpath("//ul[@class='sub']/li[3]").click()
            #切换到表单返回内容的frame
            self.driver.switch_to_frame('iframeautoheight')
            #选择框选择
            select_year = self.driver.find_element_by_xpath("//select[@id='ddlXN']")
            Select(select_year).select_by_value('2015-2016')
            select_semester = self.driver.find_element_by_xpath("//select[@id='ddlXQ']")
            Select(select_semester).select_by_value('2')
            select_course_nature = self.driver.find_element_by_xpath("//select[@id='ddl_kcxz']")
            Select(select_course_nature).select_by_value('01')
            #最后点击按钮提交表单
            elem_semester_result = self.driver.find_element_by_xpath("//input[@id='btn_xq']").click()
        except NoSuchElementException, e:
            print e
            print '定位失败'

#正则并不会玩，只能笨拙的用selenium定位了。。。
    def getInfo(self):
        #page = self.driver.page_source

        try:
            #course = self.driver.find_element_by_xpath("//table[@id='Datagrid1']/tbody/tr")
            #credit = course.find_elements_by_xpath("//table[@id='Datagrid1']/tbody/tr/td")
            # print  self.driver.find_element_by_xpath("//table[@id='Datagrid1']/tbody/tr["+index+"]/td["+item+"]").text
            courses = self.driver.find_elements_by_xpath("//table[@id='Datagrid1']/tbody/tr")
            attributes = courses[0].find_elements_by_xpath("./td")
            sum = 0
            for i in range(2, len(courses)):
                data = courses[i].find_elements_by_xpath("./td")
                self.credit.append(data[8].text)
            for item in self.credit:
                print item
            # print sum
        except NoSuchElementException, e:
            print e

        # self.driver.find_element_by_xpath("//table[@id='Datagrid1']/tbody/tr[2]").text[i]




if __name__ == '__main__':
    resultSpider = ResultSpider()
    username = '15408500124'
    password = 'gd321...'
    resultSpider.login(username, password)
    resultSpider.activeInfo()
    transcript = resultSpider.getInfo()

