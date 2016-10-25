# -*- coding:utf-8 -*-

import os
from PIL import Image
import pytesser
from PIL import ImageEnhance

'''
#把彩色图像转化为灰度图像。RBG转化到HSI彩色空间，采用I分量：
img = Image.open('CheckCode.gif')
imgry = img.convert('L')

#img.show()

#二值化处理

#       二值化是图像分割的一种常用方法。在二值化图象的时候把大于某个临界灰度值的像素灰度设为灰度极大值，
#把小于这个值的像素灰度设为灰度极小值，从而实现二值化（一般设置为0-1）。
#根据阈值选取的不同，二值化的算法分为固定阈值和自适应阈值，这里选用比较简单的固定阈值。

#把像素点大于阈值的设置,1，小于阈值的设置为0。生成一张查找表，再调用point()进行映射。
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
#out.show()

text = pytesser.image_to_string(out)
print text
'''


'''
#os.chdir(os.path.dirname('D:\\workspace\\practice\\1016'))

image = Image.open('CheckCode.gif')
enhancer = ImageEnhance.Contrast(image)
image_enhance = enhancer.enhance(4)
print pytesser.image_to_string(image)
'''

'''
def getVerify(name):
    #转化到灰度图
    im = Image.open(name)
    imgry = im.convert('L')
    #保存图像
    imgry.save('tran'+name)
    #二值化处理
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    #再次保存图像
    out.save('2'+name)
    #识别
    text = pytesser.image_to_string(out)
    print text

getVerify('CheckCode.gif')
'''

#处理复杂验证码

#噪点去除
#1.先用PIL对图像做一次图像增强,因为原图中数字的边缘和背景中的噪声并不是太分明,
# 做了增强之后能将两者分离.如果不分离,可能会在去噪点的时候导致数字中有部分会缺失
im = Image.open('CheckCode.gif')
im = ImageEnhance.Sharpness(im).enhance(3)






