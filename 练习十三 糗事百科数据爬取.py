# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:26:02 2018
URL(Uniform Resource Locator,统一资源定位符)本地、网络 路径
baidu.com
www.baidu.com
http://www.baidu.com-----------------------标准的URL
读我.txt
d:/qqyu/读我.txt
file:///d:/qqyu/读我.txt-------------------标准的URL

打开网页有几种可能性：
正常情况--OK（200）
对方挂了
自己网络问题
data=r.urlopen(url).read().decode('utf-8')#简单粗暴的方式，会出现很多问题

############题目
题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
3.下载图片。想做就做


@author: Administrator
"""
import urllib.request as r#导入URL工具包 并且命令为r
myconn=r.urlopen('http://www.baidu.com')
if myconn.getcode()==200:
    data=myconn.read().decode('utf-8')
    print(data)
else:
    print('无法访问此网站')
myconn.close()

"""
raise RemoteDisconnected("Remote end closed connection without"
RemoteDisconnected: Remote end closed connection without response
爬虫里面非常关键的：反爬虫
1.直接屏蔽程序爬取数据
2.如果访问对方服务器次数过大，对方会屏蔽你的IP/屏蔽十分钟....

"""
req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')

pat='<div class="content">(.*?)</div>'
import re
ls=re.compile(pat,re.S).findall(data)

url='https://pic.qiushibaike.com/system/pictures/11292/112920206/medium/app112920206.jpg'
r.urlretrieve(url,'./tmp.jpg')#retrieve下载文件
"""
题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
3.下载图片。想做就做
"""
import urllib.request as r#导入URL工具包 并且命令为r
import re
for i in range(0,13):
    req=r.Request('https://www.qiushibaike.com/'.format(i),headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
    myurl=r.urlopen(req)
    print(myurl.getcode())
    data=myurl.read().decode('utf-8')
    ls=re.compile('alt="(.*?)">').findall(data)
    ls1=re.compile('<div class="content">(.*?)</div>',re.S).findall(data)
    for i in range(len(ls1)):
        print('作者：{}\n内容：{}\n'.format(ls[i],ls1[i]))
    
























