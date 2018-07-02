# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:20:55 2018

@author: Administrator
"""


=====================一定要注意文件格式，保存的时候为utf-8
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序

@author: Administrator
"""
print('火车站三字码是：'+'BJX')

"""
    ls=open('./火车站编码.csv','r').readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xf8 in position 6572: illegal multibyte sequence



def hanzi_to_pin(s):
    ls=open('C:\\Users\\Administrator\\Desktop\\火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc
import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#成都
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#北京
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-28&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-28&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
#将火车站三字码替换成城市名map{}
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']
print('历时排序\n')
p='  '
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注{}'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
"""
for i in range(0,8):
    s=data[i]
    ls=s.split('|')
    #车次   车发站，到达站 出发时间,到达时间 历时间
    ls=[ls[3],[ls[6],ls[5]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--',ls[23],'--',ls[26],'--',ls[28],ls[29],'--',ls[1]]
    for i in ls:
        print(str(i).center(15).replace('[','').replace(']','').replace('BXP', '北京西').replace('CDW', "成都",). replace( 'ICW',"成都东"),end='')
    print('\n')
"""
#历史排序   
less=[]
for i in range(0,8):
    s=data[i]
    ls=s.split('|')
    #车次   车发站，到达站 出发时间,到达时间 历时间
    ls1=[ls[3],[ls[6],ls[5]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--',ls[23],'--',ls[26],'--',ls[28],ls[29],'--',ls[1]]
    less.append(ls1)
mysort=lambda b:b[3]
less.sort(key=mysort)
for i in range(0,8):
    less1=less[i]
    for i in less1:
        print(str(i).center(15).replace('[','').replace(']','').replace(',','').replace('BXP', '北京西').replace('CDW', "成都",).replace( 'ICW',"成都东"),end='')
    print('\n') 

