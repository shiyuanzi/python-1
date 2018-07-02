# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:40:09 2018

@author: Administrator
"""

练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%BE%B3%E9%97%A8&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
data['mods']['itemlist']['data']['auctions'][0]['raw_title']

商品名，价格，付款，店铺名,地址


Created on Fri Jun 22 14:24:06 2018
文件存储的问题，文件读取，文件操作
保存一个文本文件的操作过程：
1.打开记事本
2.写入内容
3.另存为
4.选择路径
5.写文件名
6.设置文件格式encoding
7.保存
读取文件的操作过程：
1.找到文件的路径和位置
2.双击打开

第七题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格

@author: Administrator
"""

"""
b=0
f=open('C:\\Users\\Administrator\\Desktop\\qingdaoqunzi.csv','w')
f.write('序号，店铺名,商品名,价格,销量,地址\n')
for i in range(0,100):
    import urllib.request as r
    url2='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%9D%92%E5%B2%9B&ajax=true'
    a=44*i
    url=url2.replace('0&ajax=true',str(a)+'&ajax=true')
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    l=len(data['mods']['itemlist']['data']['auctions'])
    for a in range(0,l):
        nick=data['mods']['itemlist']['data']['auctions'][a]['nick']#店铺名
        raw_title=data['mods']['itemlist']['data']['auctions'][a]['raw_title']#商品名
        view_price=data['mods']['itemlist']['data']['auctions'][a]['view_price']#价格
        view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']#销量
        item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']#地址
        b=b+1
        f.write('{},{},{},{},{},{}\n'.format(b,nick,raw_title,view_price,view_sales,item_loc))
    print('第{}页已获取数据'.format(i+1))
f.close()
print('关键词为“裙子”青岛地区前100页数据获取完成！')










