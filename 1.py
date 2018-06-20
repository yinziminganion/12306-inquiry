import requests
import re
#a = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9056")
#print(a.text)
#stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',a.text)
#print(stations)
#吉林JLL
#南京NJH
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-14&leftTicketDTO.from_station=JLL&leftTicketDTO.to_station=NJH&purpose_codes=ADULT

import requests
import json
import prettytable as pt
a = requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-14&leftTicketDTO.from_station=JLL&leftTicketDTO.to_station=NJH&purpose_codes=ADULT')
b = json.loads(a.text)
#在c中，下标对应如下：
#0：乱码 1：状态，可预订或者暂停发售 2：未知 3：车次号 4：该车次始发站 5：该车次终点站 6：查询起点 7：查询终点
#8：出发时间 9：到达时间 10：历时 11：未知，可能是是否可以网络购票，可以则为Y 12：乱码 13：像是日期 14-19：未知
#23：软卧 26：无座 28：硬卧 29：硬座 30：二等座 31：一等座 32：商务座/特等座
table = pt.PrettyTable(['车次','状态','出发时间','到达时间','历时','商务座','一等座','二等座','软卧','硬卧','硬座','无座'])
for item in b['data']['result']:
    c = str(item).split('|')
    table.add_row([c[3], c[1], c[8], c[9], c[10], c[32], c[31], c[30], c[23], c[28], c[29], c[26]])
print(table)