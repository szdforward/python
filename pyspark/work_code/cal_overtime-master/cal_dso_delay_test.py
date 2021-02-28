# coding:utf-8
"""
统计明细数据源延后出数的时间 测试
"""
import re
import time,datetime
def cal_summary_task(cur_day, dso_name):
    dir_info_list=[]
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-01 14:32 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2020-12-31")
    # 模拟重跑
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-03 13:52 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-01")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-03 16:43 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-02")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-04 18:05 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-03")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-05 19:24 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-04")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-06 19:37 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-05")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-07 18:32 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-06")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-08 17:30 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-07")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-09 17:11 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-08")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-10 15:00 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-09")
    # 模拟在期待时间内完成
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-11 06:00 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-10")
    dir_info_list.append("drwxr-xr-x   - analysis supergroup          0 2021-01-12 05:28 /user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-11")
    for dir_info in dir_info_list:
        str_list = re.split("\s+", dir_info) # ['drwxr-xr-x', '-', 'analysis', 'supergroup', '0', '2021-01-10', '15:00', '/user/hive/warehouse/dso.db/mobiledictclient_android/day=2021-01-09']
        if len(str_list) > 7:
            # dso明细数据源的day
            dso_day = re.findall("day=([\d-]*)", str_list[-1])[0]
            # 正常的话应该是dso_day的明天
            expect_day = (datetime.datetime.strptime(dso_day,"%Y-%m-%d") + oneday).strftime("%Y-%m-%d")
            expect_time = "%s %s:00:00"%(expect_day,expect_hour)
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
            print((dso_name,dso_day,expect_time,finish_day_time+":00", late_mins, status))
    return task_info_list
if __name__ == '__main__':
    expect_hour = str(9)
    if(len(expect_hour)==1):
        expect_hour = "0" + expect_hour
    oneday = datetime.timedelta(days=1)
    task_info_list=[]
    dso_tables = [{"group_name":"dict","members":["deskdict"]}]
    for dso_table in dso_tables:
        group_name=dso_table["group_name"]
        members=dso_table["members"]
        for dso_name in members:
            task_info_list = cal_summary_task("2021-01-10", dso_name)
        # print(task_info_list)

