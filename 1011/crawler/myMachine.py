# -*- coding:utf-8 -*-

import os
from os.path import join, getsize

rootdir = 'D:\\workspace\\practice\\1011'   #指明被遍历的文件夹

for parent, dirnames, filenames, in os.walk(rootdir):   #三个参数，分别返回目录1.父目录 2.所有文件夹名字 3.所有文件名字

    for dirname in dirnames:                            #输出目录信息
        print 'parent is:' + parent
        print 'dirname is:' + dirname

    for filename in filenames:                          #输出文件信息
        print 'parent is:' + parent
        print 'filename is:' + filename, getsize(join(parent, filename)), 'bytes'
        #输出文件路径信息


    '''
    print parent, "consumes",
    print sum(getsize(join(parent, name)) for name in filenames),
    print "bytes in", len(filenames), "non-directory files"
    if 'CVS' in dirnames:
        dirnames.remove('CVS')  # don't visit CVS directories
    '''
