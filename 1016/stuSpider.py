# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import pytesser

class Stu:
    def __init__(self):
        #self.loginUrl = "http://218.75.197.124:83/default2.aspx"
        #self.loginUrl = "http://218.75.197.124:83/xs_main.aspx?xh=15408500124"
        self.loginUrl = "http://218.75.197.124:83/xs_main.aspx?xh=15408500124#a"
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            '__VIEWSTATE' : 'dDwyODE2NTM0OTg7Oz4EGChQ14ySKRdWFtft/5U8oZidAQ==',
            'txtUserName' : '15408500124',
            'TextBox2' : 'NC1284526746',
            'txtSecretCode': 'b0kc',
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))


    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            #data = self.postdata
        )
        result = self.opener.open(request)
        #print login content
        print result.read().decode('gbk')

if __name__ == '__main__':
    stu = Stu()
    stu.getPage()

