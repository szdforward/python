#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
具体的使用就是从一个表里面查出一列字符串类型的日期，其中有2020-12 、 2020-05-02 、 2019/12/27 - 2020/01/02 这三种类型的，
其中：
2020-12 会处理之后返回 ['2020-12-01', '2020-12-02',…'2020-12-31']
2020-05-02 会处理之后返回 2999-01-01
2019/12/27 - 2020/01/02 会处理之后返回对应时间期间的数据：  ['2019-12-27', '2019-12-28', '2019-12-29', '2019-12-30', '2019-12-31', '2020-01-01', '2020-01-02']
"""
import re
# 匹配正则表达式

def funRe(line,tbl):
    matchObj  = re.match('"product":"(.*)"'+'.*'+tbl+'.*',line)
    if matchObj:
        print(matchObj.group(1) + '\t' + tbl)
        return True
    else:
        return False

# funRe()

import datetime as dt
# 获取此月份的所有日期 例如输入2020-12 的话，得到的结果为：['2020-12-01', '2020-12-02', '2020-12-03', '2020-12-04', '2020-12-05', '2020-12-06'…  这应该是一个字符串数组
# 从下面创建的udf函数udf_get_days_between也可以看到，输出的类型为ArrayType(StringType())  （szd-应该是输出的类型吧？）
def days_from_month(s):
    y = int(s.split("-")[0])
    m = int(s.split("-")[1])
    if m == 12:
        start_date = dt.datetime(year=y,month=m,day=1)
        end_date = dt.datetime(year=y+1,month=1,day=1)
        print((end_date-start_date).days)
        return([(start_date + dt.timedelta(days=d)).strftime("%Y-%m-%d") for d in range((end_date-start_date).days)])
    else:
        start_date = dt.datetime(year=y,month=m,day=1)
        end_date = dt.datetime(year=y,month=m+1,day=1)
        return([(start_date + dt.timedelta(days=d)).strftime("%Y-%m-%d") for d in range((end_date-start_date).days)])

def days_from_week(s):
    start_date = dt.datetime.strptime(s.split("-")[0].strip(),'%Y/%m/%d')
    end_date = dt.datetime.strptime(s.split("-")[1].strip(),'%Y/%m/%d')
    return([(start_date + dt.timedelta(days=d)).strftime('%Y-%m-%d') for d in range((end_date-start_date).days+1)])

def get_days_between(s):
    if len(s) <=7:
        return days_from_month(s)
    elif len(s)==23:
        return days_from_week(s)
    else:
        return [dt.datetime(year=2999,month=1,day=1).strftime('%Y-%m-%d')]

print(days_from_week("2019/12/27 - 2020/01/02"))
print(dt.datetime(year=2999,month=1,day=1).strftime('%Y-%m-%d'))