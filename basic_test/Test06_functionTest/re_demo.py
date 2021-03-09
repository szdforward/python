#!/usr/bin/env python
# coding: utf-8

import re
dir_info="drwxr-xr-x   - analysis supergroup          0 2021-01-10 15:00 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-09"
str_list = re.split("\s+", dir_info)
print(str_list,len(str_list))#['drwxr-xr-x', '-', 'analysis', 'supergroup', '0', '2021-01-10', '15:00', '/user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-09']
dso_day = re.findall("day=([\d-]*)", str_list[-1])[0]
# dir_time_day = str_list[5][0:4] + str_list[5][5:7] + str_list[5][8:10]
# print("dir_name_day:"+dir_name_day)
print("dso_day:"+dso_day)