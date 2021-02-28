# coding:utf-8
"""
统计明细数据源延后出数的时间  只能统计延迟出数据的时间，如果今天到点了还没有出来的话，不会显示失败，这个看下是否能优化下
"""
import sys,importlib
importlib.reload(sys)
sys.setdefaultencoding('utf8')
#  以上参考：https://www.cnblogs.com/bestween/p/11186988.html  reload是python2.x的使用
import re
from datetime import time,datetime
import json
# import MySQLdb # 这是python 2.x的mysql用法 python3.x的话使用PyMySQL
import PyMySQL
import subprocess
def cal_summary_task(cur_day, dso_name):
    console_res = subprocess.Popen("hadoop fs -ls /user/hive/warehouse/dso.db/" + dso_name + " | tail -n 10",
                           shell=True, stdout=subprocess.PIPE) # 更新最近10天的明细数据源的出数时间
    console_res_str = console_res.stdout.read()
    dir_info_list = console_res_str.split("\n")
    for dir_info in dir_info_list:
        # ['drwxr-xr-x', '-', 'analysis', 'supergroup', '0', '2021-01-10', '15:00', '/user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-09']
        str_list = re.split("\s+", dir_info)
        if len(str_list) > 7:
            # dso明细数据源的day
            dso_day = re.findall("day=([\d-]*)", str_list[-1])[0]
            # 正常的话应该是dso_day的明天
            expect_day = (datetime.strptime(dso_day,"%Y-%m-%d") + oneday).strftime("%Y-%m-%d")
            expect_time = expect_day + " " + expect_hour + ":00:00"
            expect_ts = time.mktime(time.strptime(expect_day + " " + expect_hour, "%Y-%m-%d %H"))
            # 明细数据源的实际完成时间
            finish_day = str_list[5]
            finish_day_time = str_list[5] + " " + str_list[6]
            finish_ts = time.mktime(time.strptime(finish_day_time, "%Y-%m-%d %H:%M"))
            late_mins = 0
            status = "success"
            # 考虑到有重跑数据的情况，
            # 1、如果完成时间跟dso_day的明天一致的话，判断延迟分钟数，有延迟的话计算延迟分钟，没有延迟的话，设定late_mins=0
            # 2、如果完成时间跟dso_day的明天不一致的话，认为这是重跑的任务，设定status=overwrite，late_mins=-0.001（可能会有明细数据源后天才出来，这种情况应该极少，暂时认定为重跑吧）
            if finish_day != expect_day:
                status = "overwrite"
                late_mins = -0.001
            elif finish_ts > expect_ts:
                late_mins = (finish_ts - expect_ts) / 60
            task_info_list.append((dso_name,dso_day,expect_time,finish_day_time+":00", late_mins, status))
    return task_info_list
if __name__ == '__main__':
    cur_day = sys.argv[1]
    expect_hour = str(sys.argv[2])
    if(len(expect_hour)==1):
        expect_hour = "0" + expect_hour
    oneday = datetime.timedelta(days=1)
    db = PyMySQL.connect("10.109.xxx", "root", "xxx", "db_calculate_overtime", charset='utf8')
    cursor = db.cursor()
    task_info_list=[]
    dso_tables = [{"group_name":"dict","members":["deskdict"]}]
    for dso_table in dso_tables:
        group_name=dso_table["group_name"]
        members=dso_table["members"]
        for dso_name in members:
            task_info_list = cal_summary_task(cur_day, dso_name)
        for task_info in task_info_list:
            dso_name = task_info[0]
            dso_day = task_info[1]
            expect_time = task_info[2]
            finish_time = task_info[3]
            late_mins = str(task_info[4])
            status = task_info[5]
            insert_sql = "INSERT INTO dso_delay (group_name,dso_name,dso_day,expect_time,finish_time,late_mins,task_status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
                .format(group_name, dso_name, dso_day, expect_time, finish_time, late_mins, status)
            cursor.execute(insert_sql)
            print(insert_sql)
    db.commit()
    db.close()

