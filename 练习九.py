# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:16:50 2018

@author: Administrator
"""

中国铁路火车票上的车次，有以C（读作“城”）打头的车次、
以D（读作“动车”）打头的车次、
以G（读作“高”）打头的车次、-------------------------------OK
以N（读作“内”）打头的车次、
以Z（读作“直”）打头的车次、
以T（读作“特”）打头的车次、
以K（读作“快”）打头的车次、
以L（读作“临”）打头的车次、
以Y（读作“游”）打头的车次和不带字母打头的车次等十余种。
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-26&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']
p='  '
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()

for i in range(9):#print('第几次循环'.format(i+1))
    s=data['data']['result'][i]
    ls=s.split('|')
    if ls[3].startswith('G'):
#车次   车发站，到达站 出发时间,到达时间 历时间
        ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
        for i in ls:
            print(str(i).center(15).replace('[','').replace(']',''),end='')
        print('\n')

#print('车次')
#print('ab')




s='N%2FySZswGXDqQPNR7KNqFwdBzvUwW%2Bl82FYFZ2hPdxUzg7dzpUdnAg2pq834pT2qxTxBpKYtUuHR0%0A%2FnW0SyuTkQBbT%2F4eQ77ZOW%2BtoKzu3wXAhd4uf4mUaXR1Yse3VS12QsN8ldXNn0NHYVwhbd7O2eW4%0AllD120G3NZiO%2FJsOiBpLp4zQ4QDtmRuAjMw9DdUyAs1m5xmrupP%2BsBCvBsljceSxMbjrmB2Pq2Gd%0ANnbvHm71zWRAdhG33ssxwkoMBNBU|预订|2400000G890B|G89|BXP|ICW|BXP|ICW|06:53|14:41|07:48|Y|I6f4%2F%2FVjmDh8FowzPFKFCfA38qy9Ynseatx1cYr0%2BTgDl0aA|20180626|3|P4|01|05|1|0|||||||||||有|19|1||O0M090|OM9|0'
ls2=s.split('|')

s='6nMecwwn%2FmtGuiPXKYxmT0FbbWWTvjF2UAaua033kdXVop408GE72Z0Fufh9%2BpIuEhIljbPBM5to%0AeTNk4ueWtfua5a3rTPfElUhDj2nUJsIc10AB%2B2Z6qteAs%2FcxgwcacnCL2RrIk3ECIB828Dc8NgOT%0Afl9aA60YO3fhi7afiBmwG6dGzDZNrBeuJsf19kj2%2FGIV9RwIle2l5ZSEE%2BnrJNZ6KPk3x9jmrzul%0Ana%2BW5R%2BKhCVf1klsJh0DiJcOC331|预订|240000G1010F|G101|VNP|AOH|VNP|NKH|06:43|11:14|04:31|Y|anKuw6ZIFPhViJi9kL%2Bo3KEA4Mj6oqybYA9LVMScFH3GP0MH|20180717|3|P2|01|08|1|0|||||||||||有|有|9||O0M090|OM9|0'
ls3=s.split('|')







