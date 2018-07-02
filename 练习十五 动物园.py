# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:53:44 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

@author: Administrator
"""
monkey={"绰号":'星期五','公母':'公','毛色':'黄色','猴龄':'3'}

print(monkey['绰号'])
monkey.suanshu(1,1)
#####这就是一个类，猴子类
class Monkey:
    #猴子对象产生的时候，会调用这个方法Monkey()
    def __init__(self,name,sex,color,age):#########系统固定的方法
        self.name=name
        self.sex=sex
        self.color=color
        self.age=age
    def calc(self,x,y):#self 有对象
        print(x+y)
    def bike(self):
        print(self.name+'猴子以20迈的速度正在前进')
a=Monkey('星期五','公','黄色','3')
print(a.name)
print(a.sex)
print(a.color)
print(a.age)################静态信息
a.calc(1,1)
b=Monkey('灵明石猴','公','黄色','800')
b.bike()
"""
题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法
"""
#1
Weather={}
class Weather:
    def __init__(self,data,temp,description,pre):#########系统固定的方法
        self.data=data
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):#self 有对象
        print('日期:{} 温度:{} 天气情况：{}  气压：{}'.format(self.data,self.temp,self.description,self.pre))
a=Weather('2018-06-30','21','晴','1013.1')
b=Weather('2018-07-01','21','多云','1021.1')
c=Weather('2018-07-02','22','晴','1314')
a.msg()
b.msg()
c.msg()
#2
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=yantai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
class Weather:
    def __init__(self,city,data,temp,description,pre):
        self.city=city
        self.data=data
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):#self 有对象
        print('city：{}  time:{}  temp:{} description：{}  pre：{}'.format(self.city,self.data,self.temp,self.description,self.pre))   
for i in (2,10,18):
    g=data['city']['name']
    b=data['list'][i]['dt_txt']
    c=data['list'][i]['main']['temp']
    d=data['list'][i]['weather'][0]['description']
    e=data['list'][i]['main']['pressure']
    a=Weather(g,b,c,d,e)
    a.msg()    
















