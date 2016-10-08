# -*- coding:utf-8 -*-
import os

accout_file = 'accounts.txt'
lock_file = 'lock.txt'

fp = open("test.txt", 'r+')

userIf = False  #判断是否匹配了用户名
userTr = False  #判断用户名是否输入正确

passIf = False  #判断是否匹配了密码
passTr = False  #判断密码是否输入正确

count = 0   #记录失败次数

print '欢迎登录！'
print '请在下方输入用户名和密码'

while True:
    username = raw_input('请输入用户名：') 
    password = raw_input('请输入密码：')

    print '验证中...'

    for line in fp:
        if userIf == False:
            userIf = True
            passIf = False
            print line, username, type(line), type(username)
            if line == username:
                print 'y'
                userTr = True
                passIf = False
        elif passIf == False:
            passIf = True
            userIf = False
            #print line, password
            if line == password:
                passTr = True

    if userTr == True & passTr == True:
        print '登录成功！'
        break
    else:
        print '用户名或密码不正确！'
        print userTr, passTr
        count += 1
        if count == 3:
            print '错误次数达到3次，该账号已锁定'
            break

fp.close()