# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:54:44 2018

@author: Administrator
"""
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng- 学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定

#1根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
ls=re.compile('jianjie-(.*?).html').findall(s)
ls1=re.compile('(.*?)http').findall(s)
for i in range(2300):
    print("编号：{} 学校：{}".format(ls[i],ls1[i]))

f=open('./c.csv','w')
for i in range(2300):
    f.write(ls[i])

f.close()

#2.根据http://www.gaokaopai.com/daxue-zhaosheng- 学校编号.html 获取全国城市的编号 例如北京：11
      
import urllib.request as r
url='http://www.gaokaopai.com/daxue-zhaosheng-477.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import re
a=re.compile('<li data-val="(.*?)" data-id="2"').findall(d)
b=re.compile(".setVar\S.claimCity',(.*?)\S\S>").findall(d)
for i in range(31):
    print('省份:{},编号:{}'.format(a[i],b[i]))


   
#开始爬数据
import urllib.request as r
import json
f=open('./rs3.txt','w')
for i in range(2300):
    try:
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
        data='id={}&type=2&city=61&state=1'.format(ls[i]).encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        ls3=json.loads(d)
        for i in range(len(ls3['data'])):
            a1=ls3['data'][i]
            f.write('{}'.format(a1))
        f.write('\n')
    except Exception as err:
        print('')    
f.close()



#最终版14.3
f=open('C:\\Users\\Administrator\\Desktop\\all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
f.close()    
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=63&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=63&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))
        continue
f=open('./青海文科3.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()


        
###地区招生人数
##字典
a=0
b=0
f=open('./青海文科3.txt','r',encoding='utf-8')
s=f.readlines()#将所有的文本中的每行读取到一个列表中去
import json
for i in range(len(s)):
    s[i]=json.loads(s[i])
    if s[i]['status']==1:
       ls=len(s[i]['data'])
       for a in range(ls):
           b=b+int(s[i]['data'][a]['plan'])             
print('青海文科人数是：{}'.format(b))
##正则
f=open('./青海文科3.txt','r',encoding='utf-8')
s=f.read()
import re
ls=re.compile('plan":"(.*?)","uniname').findall(s)
a=0
for i in range(len(ls)):
    a=a+int(ls[i])
print('青海文科人数是：{}'.format(a))
