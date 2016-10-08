# -*- coding:utf-8 -*-
import sys

accout_file = 'accounts.txt'
lock_file = 'lock.txt'

match_flag = False

count = 0   #记录失败次数

print '欢迎登录！'
print '请在下方输入用户名和密码'

while True:
    username = raw_input('请输入用户名：') #当用户输入用户名后检查此用户是否lock
    lock_check = file(lock_file)

    for line in lock_check.readlines(): #循环lock文件
        if username in line:
            lock_check.close()  #在退出之前先关闭打开的文件
            sys.exit('\033[31;1mUser %s is locked!' % username) #如果locked就直接退出

    lock_check.close()  #文件打开后要关闭

    password = raw_input('请输入密码：')
    print '验证中...'

    f = file(accout_file, 'rb')

    for line in f.readlines():
        user, passwd = line.strip('\n').split()
        #去掉每行多余的\n，并把这一行按空格分成两列，分别赋值为user, passwd两个变量

        if username == user and password == passwd:
            print 'Match!', username
            match_flag = True
            f.close()
            break

    if match_flag:
        print '登录成功！'
        break
    else:
        print '用户名或密码不正确！'
        count += 1
        if count == 3:
            lock_c = file(lock_file, 'ab')
            lock_c.write('\n' + username)
            print '错误次数达到3次，该账号已锁定'
            break

