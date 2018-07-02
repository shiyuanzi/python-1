# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:51:37 2018

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
url='https://s.taobao.com/search?spm=a21bo.2017.201867-main.29.5af911d9rp25Fe&ie=utf8&initiative_id=staobaoz_20170419&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E8%BF%9B%E5%8F%A3%E7%8B%97%E7%B2%AE&suggest=history_3&_input_charset=utf-8&wq=&suggest_query=&source=suggest&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
for i in range(0,35):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][i]['nick']
    e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    print('商品名:{},价格:{},付款:{},店铺名:{},地址:{}'.format(a,b,c,d,e))
for i in range(0,35):
    i=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    print(i)

import re
#价格排序
ls=[]
for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    b=float(a)
    ls.append(b)
sorted(ls)
ls1=sorted(ls,reverse=True) 
print(ls1)
#销量排序
import re
ls=[]
for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    b=re.sub('\D','',a)
    c=float(b)
    ls.append(c)
sorted(ls)
ls1=sorted(ls,reverse=True) 
print(ls1)
#商品过滤，包邮的商品
for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if a=="0.00":
        try:
            b=data['mods']['itemlist']['data']['auctions'][i]['icon'][iconPopupComplex][subIcons][0][icon_content]
        except Exception as err:
            if(b=='15天退货'):
                print('商品:{},包邮,提供:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['raw_title'],b))

   