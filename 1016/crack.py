# -*- coding:utf-8 -*-

from PIL import Image
import pytesser


#im2 = Image.open('crack.gif')




# 将图片转换为8位像素模式  ,这个失败了，本来是convert("P")
im = Image.open('CheckCode.gif')
im = im.convert("L")
im2 = Image.new("L", im.size, 255)
his = im.histogram()
values = {}
# 神级算法...咳咳，试了那么多只有这个成功了，效果还行
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 17: # these are the numbers to get
            im2.putpixel((y, x), 0)

im2.save('crack1.gif')
text = pytesser.image_to_string(im2)
print text

#
# for i in range(256):
#     values[i] = his[i]
# for j, k in sorted(values.items(), key=lambda x:x[1], reverse=True)[:10]:
#     print j, k
#
#     255 *
#     1227
#     17 *
#     215 --
#     184 --
#     84
#     209 --
#     80
#     199 --
#     21
#     249
#     20
#     178
#     18
#     113
#     16
#     153
#     16
#     239
#     15

