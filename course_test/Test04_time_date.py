# coding=utf-8


#获取当前时间，例如：
import time, datetime;
# localtime = time.localtime(time.time())
# print("Local current time :",localtime) # Local current time : time.struct_time(tm_year=2020, tm_mon=12, tm_mday=6, tm_hour=13, tm_min=1, tm_sec=6, tm_wday=6, tm_yday=341, tm_isdst=0)
# #说明：time.struct_time(tm_year=2014, tm_mon=3, tm_mday=21, tm_hour=15, tm_min=13, tm_sec=56, tm_wday=4, tm_yday=80, tm_isdst=0)属于struct_time元组
# #
# #获取格式化的时间
# #可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
# #日期转换为字符串
# print(time.asctime()) # Sun Dec  6 13:03:24 2020
# #首选：
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # 2020-12-06 13:01:06
# #其次：
# print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')) # 2020-12-06 13:01:06
# #最后：
# print(str(datetime.datetime.now())[:19]) # 2020-12-06 13:01:06
# #字符串转换为日期
# expire_time = "2013-05-21 09:50:35"
# d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
# print(d) # 2013-05-21 09:50:35

#获取日期差
#
oneday = datetime.timedelta(days=1)
print(oneday) # 1 day, 0:00:00
print(datetime.timedelta(milliseconds=1),) #1毫秒   0:00:00.001000
print(datetime.timedelta(seconds=1),) #1秒   0:00:01
print(datetime.timedelta(minutes=1),) #1分钟 0:01:00
print(datetime.timedelta(hours=1),) #1小时  1:00:00
print(datetime.timedelta(days=1),) #1天  1 day, 0:00:00
print(datetime.timedelta(weeks=1))#  7 days, 0:00:00
##今天
today = datetime.date.today()
#昨天
yesterday = datetime.date.today() - oneday
##明天
tomorrow = datetime.date.today() + oneday
#上周
other = datetime.date.today()- datetime.timedelta(weeks=1)
print(today,yesterday,tomorrow) # 2020-12-06 2020-12-05 2020-12-07
print("other: ",other) # other:  2020-11-29
##获取今天零点的时间
today_zero_time = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
print(today_zero_time) # 2020-12-06 00:00:00
print("time.strftime:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1463795435)))
#获取上个月最后一天
last_month_last_day = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1) # 2020-11-30
print(last_month_last_day)
#字符串日期格式化为秒数，返回浮点类型：
expire_time = "2016-05-21 09:50:35"
d = datetime.datetime.strptime(expire_time,"%Y-%m-%d %H:%M:%S")
time_sec_float = time.mktime(d.timetuple())
print(time_sec_float) # 1463795435.0  注意得到的是秒值!

# time的使用
hour = "9"
finish_ts=1606782400.0
time_tup = time.strptime("2020" + "-" + "12" + "-" + "01" + " " + hour, "%Y-%m-%d %H")
standard_ts = time.mktime(time_tup)
print(standard_ts)
late_mins = (finish_ts - standard_ts) / 60 #if finish_ts > standard_ts else 0
print(late_mins)