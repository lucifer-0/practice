# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib


#验证码地址和post地址
CaptchaUrl = 'http://218.75.197.124:83/CheckCode.aspx'
PostUrl = 'http://218.75.197.124:83/default2.aspx'
url = 'http://218.75.197.124:83/xs_main.aspx?xh=15408500124'

#将cookies绑定到一个opener. cookie 由cookielib管理
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

#用户名和密码
username = '15408500124'
password = ''

#用opener访问验证码地址获取cookie
image = opener.open(CaptchaUrl).read()
#image = urllib.urlopen(CaptchaUrl)

#保存验证码到本地
file = open('check.gif', 'wb')
file.write(image)
file.close()

checkCode = raw_input('请输入验证码：')

#根据抓包信息构造表单
postData = {
    '__VIEWSTATE':'dDwyODE2NTM0OTg7Oz4EGChQ14ySKRdWFtft/5U8oZidAQ==',
    'txtUserName':username,
    'TextBox2':password,
    'txtSecretCode':'apu0',
    'RadioButtonList1':'学生',
    'Button1':'',
    'lbLanguage':'',
    'hidPdrs':'',
    'hidsc':'',
}

#根据抓包信息构造Headers
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
#生成post数据 ?key1=value&key2=value的形式
data = urllib.urlencode(postData)
#request请求
request = urllib2.Request(PostUrl, data, headers)
try:
    response = opener.open(request)
    result = response.read().decode('gb2312')   #由于该网页是gb2312的编码，所以需要解码
    print result
except urllib2.HTTPError, e:
    print e.code


























