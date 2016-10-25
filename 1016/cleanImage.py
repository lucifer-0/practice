# -*- coding:utf-8 -*-

from PIL import Image, ImageFilter, ImageEnhance
import subprocess

'''
def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    # Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    # call tesseract to do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "output"])

    # Open and read the resulting data file
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()


cleanFile("CheckCode.gif", "CheckCode_clean.gif")
'''

image_name = 'CheckCode.gif'

im = Image.open(image_name)
imgry = im.convert('L')
imgry = imgry.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(imgry)
imgry = enhancer.enhance(2)

im.show()
