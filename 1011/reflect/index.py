# -*- coding:utf-8 -*-

url_data = raw_input('请输入地址：')
array = url_data.split('/')

user_spance = __import__('reflect.' + array[0])

model = getattr(user_spance, array[0])

func = getattr(model, array[1])

func()