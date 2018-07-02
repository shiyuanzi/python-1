# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:53:22 2018

@author: Administrator
"""
练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。
  ls=['当山峰没有棱角的时候','当河水不再流','当时间停住日夜不分',
'当天地万物化为虚有']
print('wo' in ls)
print('当山峰没有棱角的时候' in ls)
#这种循环和列表很搭  
for line in ls:
    print(line)
    
ls=range(9)
for i in ls:
    print(i)

for i in range(0,9,1):
    print(i)

for i in range(0,9,2):
    print(i)

#固定次数的循环和列表和搭配
#还有一种循环，是没有次数限制的。有死循环，
for i in range(0,9999999999):
    print(i)

while True:#当什么时候
    print('kdlfjdkfjlkd')


############################
for i in range(1,101):
    print('跑第{}圈'.format(i))
    if i==3:
        break
    
for i in range(1,101):
    if i==10:
        print('幸运通道，执行进入下一次')
        continue
    print('跑第{}圈'.format(i))

###########
for i in [1,2,3]:
    print(i)
    for j in [0.1,0.2,0.3]:
        print(j)

"""
1------i
0.1----j
0.2----j
0.3----j
2------i
0.1----j
0.2----j
0.3----j
3------i
0.1----j
0.2----j
0.3----j
"""
##
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=yantai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
for i in range(0,24,3):
    b=data['list'][i]['dt_txt']
    c=data['list'][i]['main']['temp']
    d=data['list'][i]['weather'][0]['description']
    e=data['list'][i]['main']['pressure']
    g=data['list'][i]['main']['temp_max']
    print('时间{},温度{},天气情况{},气压{},最高温度{}'.format(b,c,d,e,g))
    if c>=25:
        print('温馨提醒：天气炎热，注意防晒，出门可戴遮阳帽')
    elif c>=22:
         print('温馨提醒：天气凉爽')
    elif c>=20:
         print('温馨提醒：天气凉爽，适合户外运动')  
         
         
for i in ['天','气','小','贴','士','!']: 
    print('❥(^_-)'*3,i,'❥(^_-)'*3)

ctrl+f5,调试文件
进入下一行,运行当前行ctrl+f10
运行到下一个断点。ctrl+f12
@author: Administrator
"""

for i in [1,2,3]:
    print(i)
    for j in [0.1,0.2,0.3]:
        print(j)
print('end')
















