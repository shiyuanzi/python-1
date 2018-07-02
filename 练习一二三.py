# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
第一题
c=['22','21','20','22','23','25','22']
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
print(c[5])
print(c[6])
print("星期三是："+str (c[2]))
第二题
msg={'温度':['22','21','20','22','23','25','22'],'天气':['晴','雨','雨','晴','雨','雨','雨'],'最高温度':'30'}
msg['温度'][2]
msg['天气'][2]
msg['最高温度']
第三题
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
data['main']['temp']
data['weather'][0]['description']
data['main']['pressure']
print('重庆温度是：'+str(data['main']['temp']))
print('重庆天气情况是：'+str(data['weather'][0]['description']))
print('重庆天气气压是：'+str(data['main']['temp']))