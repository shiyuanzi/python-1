# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他


@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=b75ea8bf00054988&rsv_t=dd9ayXxS7dBRFkeQivUcpx2d1SN3eyFM49rJXgYU7qeumVfQGLHsKRjuJJM&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&inputT=979&rsv_sug4=2969&rsv_sug=2'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
"""
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%8E%89%E5%AE%B3%E4%BA%86%E6%88%91%E7%9A%84%E5%9B%BD%20%E9%87%8D%E5%BA%86&rsv_pq=e3da85070001e935&rsv_t=204bDTCNe075%2FBiCOglZ97%2F6S3WVVzuFV0K0R9DJjCqb1ACHur89PPDyYVE&rqlang=cn&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsp=8&rsv_sug9=es_1_1&rsv_sug4=2856&rsv_sug=9'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
ls1=re.compile('class="c-abstract">(.*?)</div>').findall(data)#爬取标题下的描述
ls2=re.compile('style="text-decoration:none;">(.*?)</a>').findall(data)#搜索的标题的网站
for i in range(len(ls2)):
    print('标题是：{}\n描述是：{}\n网站是：{}\n'.format(ls[i],ls1[i],ls2[i]))
  
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=yantai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"description":"(.*?)"').findall(data)
ls1=re.compile('"temp":(.*?),').findall(data)
ls2=re.compile('"pressure":(.*?),').findall(data)
ls3=re.compile('"dt_txt":"(.*?)"').findall(data)
for i in range(36):
    print('时间{} 天气描述：{} 天气温度：{} 天气气压：{}'.format(ls3[i],ls[i],ls1[i],ls2[i]))