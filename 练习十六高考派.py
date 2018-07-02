# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 11:09:56 2018

@author: Administrator
"""

题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例
#1.根据2300下载的两百多M文件，统计招生总人数
a=0
b=0
f=open('./全国招生计划表0206C正确.txt','r',encoding='utf-8')
s=f.readlines()#将所有的文本中的每行读取到一个列表中去
import json
for i in range(len(s)):
    s[i]=json.loads(s[i])
    if s[i]['status']==1:
       ls=len(s[i]['data'])
       for a in range(ls):
           b=b+int(s[i]['data'][a]['plan'])
print('全国高校招生总人数：{}'.format(b))
#2.统计7各地域的人数各是多少
"""

"""
f=open('./全国招生计划表0206C正确.txt','r',encoding='utf-8')
s=f.readlines()#将所有的文本中的每行读取到一个列表中去
import json
zone={'山东':'华东','江苏':'华东','安徽':'华东','江西':'华东','浙江':'华东','福建':'华东','上海':'华东','广东':'华南','广西':'华南','海南':'华南','湖北':'华中','湖南':'华中','河南':'华中','北京':'华北','天津':'华北','河北':'华北','山西':'华北','内蒙古':'华北','宁夏':'西北','新疆':'西北','青海':'西北','陕西':'西北','甘肃':'西北','四川':'西南','云南':'西南','贵州':'西南','西藏':'西南','重庆':'西南','辽宁':'东北','吉林':'东北','黑龙江':'东北'}
ap={'华北':0,'华南':0,'华中':0,'华东':0,'西北':0,'西南':0,'东北':0}
for i in range(len(s)):
    s[i]=json.loads(s[i])
    if s[i]['status']==1:
       for a in range(len(s[i]['data'])):
           city=s[i]['data'][a]['city']
           plan=s[i]['data'][a]['plan']
           ap[zone[city]]=ap[zone[city]]+int(plan)
f=ap['华北']+ap['华南']+ap['华中']+ap['华东']+ap['西北']+ap['西南']+ap['东北']
print('华北招生总人数{}\n华南招生总人数{}\n华中招生总人数{}\n华东招生总人数{}\n西北招生总人数{}\n西南招生总人数{}\n东北招生总人数{}\n全国招生总人数{}\n'.format(ap['华北'],ap['华南'],ap['华中'],ap['华东'],ap['西北'],ap['西南'],ap['东北'],f))
        

    

    
    
