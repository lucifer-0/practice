# -*- coding:utf-8 -*-

print '请按格式输入，替换字符'

oldText = raw_input('请输入原字符：')
newText = raw_input('请输入替换字符：')
filename = 'password.txt'

f = file(filename, 'rb')

new_file = file('%s.bak' % filename, 'wb')

for line in f.readlines():
    new_file.write(line.replace(oldText, newText))

new_file.close()
f.close()