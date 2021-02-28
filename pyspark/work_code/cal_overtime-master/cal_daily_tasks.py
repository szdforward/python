# coding:utf-8
"""
统计概要数据源延后出数的时间
"""
import sys,importlib
importlib.reload(sys)
sys.setdefaultencoding('utf8')
#  以上参考：https://www.cnblogs.com/bestween/p/11186988.html  reload是python2.x的使用
import re
import time
import json
# import MySQLdb # 这是python 2.x的mysql用法 python3.x的话使用PyMySQL
import PyMySQL
import subprocess
def cal_jenkins_task(cur_day, task_url):
    def get_standard_ts(finish_ts):
        finish_time_struct = time.localtime(finish_ts)
        year = str(finish_time_struct.tm_year)
        mon = str(finish_time_struct.tm_mon)
        day = str(finish_time_struct.tm_mday)
        hour = "9"
        time_tup = time.strptime(year + "-" + mon + "-" + day + " " + hour, "%Y-%m-%d %H")
        standard_ts = time.mktime(time_tup)
        return standard_ts
    def get_json_str(task_url):
        # subprocess.Popen()的使用可以参照：https://www.cnblogs.com/zhoug2020/p/5079407.html
        res = subprocess.Popen("curl '" + task_url + "/api/json?tree=allBuilds\[*\]'", shell=True, stdout=subprocess.PIPE)
        json_str = res.stdout.read()
        return json_str
    json_str = get_json_str(task_url)
    json_obj = json.loads(json_str)
    all_builds = json_obj["allBuilds"]
    all_builds.reverse() # 逆序让调度早的先遍历
    res = []
    for build in all_builds: # 拿到的是近七天的15个任务，一个个遍历
        # Python3.x 版本已删除 long() 函数。https://www.runoob.com/python/python-func-long.html  在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
        submit_ts = int(build["timestamp"])
        finish_ts = (submit_ts+int(build["duration"]))/1000
        finish_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(finish_ts))
        etl_day = finish_time_str[0:10]
        if etl_day == cur_day:
            standard_ts = get_standard_ts(finish_ts)
            late_mins = (finish_ts - standard_ts) / 60 if finish_ts > standard_ts else 0
            submit_time = time.strftime("%H:%M:%S", time.localtime(submit_ts/1000))
            produced_time = finish_time_str[11:19]
            status = build["result"]
            res.append((etl_day, submit_time, produced_time, late_mins, status))
            if status == "SUCCESS":
                break # 只计算当天第一次成功的
    return res
def cal_summary_task(cur_day, hdfs_path):
    console_res = subprocess.Popen("hdfs dfs -ls /exec/analysis/druid/deepStorage_0_8_3/" + task_name + " | tail -n 30",
                           shell=True, stdout=subprocess.PIPE) # 这里限制为了一下最近30天的
    console_res_str = console_res.stdout.read()
    dir_info_list = console_res_str.split("\n")
    res = []
    for dir_info in dir_info_list:
        str_list = re.split("[ ]*", dir_info) # 拆分为权限、...、生成时间、目录名
        # str_list = re.split("\s+", dir_info) # 拆分为权限、...、生成时间、目录名   这样写匹配多个空格也许更好一些
        # ['drwxr-xr-x', '-', 'analysis', 'supergroup', '0', '2021-01-05', '07:06', '/exec/analysis/druid/deepStorage_0_8_3/mobileDictClient.aged/20210104T000000.000+0800_20210105T000000.000+0800']
        if len(str_list) > 7 and str_list[5] == cur_day:
            finish_time_str = str_list[5] + " " + str_list[6]
            finish_ts = time.mktime(time.strptime(finish_time_str, "%Y-%m-%d %H:%M"))
            standard_ts = time.mktime(time.strptime(str_list[5] + " 09", "%Y-%m-%d %H"))
            dir_name_day = re.findall("_([0-9]*)T", str_list[7])[0]
            dir_time_day = str_list[5][0:4] + str_list[5][5:7] + str_list[5][8:10]
            late_mins = 0
            status = "SUCCESS"
            if dir_time_day != dir_name_day:
                late_mins = "FAILURE"
            elif finish_ts > standard_ts:
                out_time = (finish_ts - standard_ts) / 60
            res.append((str_list[5], '', str_list[6]+":00", late_mins, status))
    return res
def cal_azk_job_task(cur_day, task_name):
    azk_db = PyMySQL.connect("analysis-db", "azkaban_secure", "azkaban_secure", "azkaban_secure", charset='utf8')
    azk_cursor = azk_db.cursor()
    azk_cursor.execute("""
                        SELECT 
                            from_unixtime(start_time/1000, '%Y-%m-%d') AS etl_day,                       
                            from_unixtime(start_time/1000, '%H:%i:%s') AS submit_time,
                            from_unixtime(end_time/1000, '%H:%i:%s') AS produced_time,
                            (end_time/1000-CAST(end_time/1000/3600/24 AS signed)*24*3600-3600)/60 AS late_mins, -- 本应该是-9*3600，因为8小时时差，所以+8*3600--合并为-》-3600
                            CASE WHEN status = 50 THEN 'SUCCESS' WHEN status = 60 THEN 'ABORTED' ELSE 'FAILURE' END AS status
                        FROM azkaban_secure.execution_jobs 
                        WHERE job_id LIKE '%{}%'
                        AND from_unixtime(start_time/1000, '%Y-%m-%d')='{}'
                        AND from_unixtime(start_time/1000, '%Y-%m-%d')=from_unixtime(end_time/1000, '%Y-%m-%d')
                        ORDER BY start_time;""".format(task_name, cur_day))
    azk_results = azk_cursor.fetchall()
    res = []
    for azk_result in azk_results:
        etl_day = azk_result[0]
        submit_time = azk_result[1]
        produced_time = azk_result[2]
        late_mins = float(azk_result[3]) if float(azk_result[3]) > 0 else 0
        status = azk_result[4]
        res.append((etl_day, submit_time, produced_time, late_mins, status))
        if status == 'SUCCESS':
            break
    return res
def cal_azk_flow_task(cur_day, task_type):
    azk_db = PyMySQL.connect("analysis-db", "azkaban_secure", "azkaban_secure", "azkaban_secure", charset='utf8')
    azk_cursor = azk_db.cursor()
    azk_cursor.execute("""
                        SELECT 
                            from_unixtime(start_time/1000, '%Y-%m-%d') AS etl_day,
                            from_unixtime(start_time/1000, '%H:%i:%s') AS submit_time,
                            from_unixtime(end_time/1000, '%H:%i:%s') AS produced_time,
                            (end_time/1000-CAST(end_time/1000/3600/24 AS signed)*24*3600-3600)/60 AS late_mins, -- 本应该是-9*3600，因为8小时时差，所以+8*3600--合并为-》-3600
                            CASE WHEN status = 50 THEN 'SUCCESS' WHEN status = 60 THEN 'ABORTED' ELSE 'FAILURE' END AS status
                        FROM azkaban_secure.execution_jobs 
                        WHERE flow_id LIKE '%{}%'
                        AND from_unixtime(start_time/1000, '%Y-%m-%d')='{}'
                        AND from_unixtime(start_time/1000, '%Y-%m-%d')=from_unixtime(end_time/1000, '%Y-%m-%d')
                        ORDER BY start_time;""".format(task_name, cur_day))
    azk_results = azk_cursor.fetchall()
    res = []
    for azk_result in azk_results:
        etl_day = azk_result[0]
        submit_time = azk_result[1]
        produced_time = azk_result[2]
        late_mins = float(azk_result[3]) if float(azk_result[3]) > 0 else 0
        status = azk_result[4]
        res.append((etl_day, submit_time, produced_time, late_mins, status))
        if status == 'SUCCESS':
            break
    return res
def cal_mammut_task(cur_day, task_type):
    mm_db = PyMySQL.connect("eadb10-writer", "mammut", "n7ZaNi8J6BADgJ1q", "mm_azkaban_eadhadoop", charset='utf8')
    mm_cursor = mm_db.cursor()
    mm_cursor.execute("set names utf8mb4")
    mm_cursor.execute("""
                        SELECT 
                            from_unixtime(start_time/1000, '%Y-%m-%d') AS etl_day,
                            from_unixtime(start_time/1000, '%H:%i:%s') AS submit_time,
                            from_unixtime(end_time/1000, '%H:%i:%s') AS produced_time,
                            (end_time/1000-CAST(end_time/1000/3600/24 AS signed)*24*3600-3600)/60 AS late_mins, -- 本应该是-9*3600，因为8小时时差，所以+8*3600--合并为-》-3600
                            CASE WHEN status = 50 THEN 'SUCCESS' WHEN status = 60 THEN 'ABORTED' ELSE 'FAILURE' END AS status
                        FROM mm_azkaban_eadhadoop.execution_flows
                        WHERE flow_id = '{}'
                        AND from_unixtime(start_time/1000, '%Y-%m-%d')='{}'
                        AND from_unixtime(start_time/1000, '%Y-%m-%d')=from_unixtime(end_time/1000, '%Y-%m-%d')
                        ORDER BY start_time;""".format(task_name, cur_day))
    mm_results = mm_cursor.fetchall()
    res = []
    for mm_result in mm_results:
        etl_day = mm_result[0]
        submit_time = mm_result[1]
        produced_time = mm_result[2]
        late_mins = float(mm_result[3]) if float(mm_result[3]) > 0 else 0
        status = mm_result[4]
        res.append((etl_day, submit_time, produced_time, late_mins, status))
        if status == 'SUCCESS':
            break
    return res
if __name__ == '__main__':
    cur_day = sys.argv[1]
    db = PyMySQL.connect("10.109.xxx", "root", "xxx", "db_calculate_overtime", charset='utf8')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_task")
# +---------+--------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------+
# | task_id | product_name | task_name                                                                                   | task_url                                                                              | task_type           |
# +---------+--------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------+
# |       2 | 精品课       | ke_kernal_order_subject_cate                                                                | http://hd020:8873/analysis/job/ke_kernal_order_subject_cate                           | jenkins             |
# |       8 | 词典         | deskdict.aged                                                                               | /exec/analysis/druid/deepStorage_0_8_3/deskdict.aged                                  | summary_data_source |
# |      14 | 国际词典     | interdict_android_action_puv                                                                | NULL                                                                                  | azkaban_job         |
# |      15 | 少儿         | ads_children_daily_roi_dd                                                                   | NULL                                                                                  | mammut              |
    results = cursor.fetchall()
    for row in results:
        print(row)
        product_name = row[1]
        task_name = row[2]
        task_url = row[3]
        task_type = row[4].encode("utf-8")
        task_info_list = []
        if task_type == 'jenkins':
            # pass实际是空语句，在python2.x中，如果定义了一个函数，但是没有函数体的话，会报错  在python3.x中可以不写，具体可见：https://www.runoob.com/python/python-pass-statement.html
            pass
            task_info_list = cal_jenkins_task(cur_day, task_url)
        elif task_type == 'summary_data_source':
            pass
            task_info_list = cal_summary_task(cur_day, task_url)
        elif task_type == "mammut":
            pass
            task_info_list = cal_mammut_task(cur_day, task_url)
        elif task_type == "azkaban_job":
            pass
            task_info_list = cal_azk_job_task(cur_day, task_name)
        elif task_type == "azkaban_flow":
            pass
            task_info_list = cal_azk_flow_task(cur_day, task_name)
        for task_info in task_info_list:
            etl_day = task_info[0]
            submit_time = task_info[1]
            produced_time = task_info[2]
            late_mins = str(task_info[3])
            status = task_info[4]
            insert_sql = "INSERT INTO tb_task_daily_info (product_name, task_name, task_type, etl_day, submit_time, produced_time, late_mins, task_status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(product_name, task_name, task_type, etl_day, submit_time, produced_time, late_mins, status)
            cursor.execute(insert_sql)
            print(insert_sql)
    db.commit()
    db.close()

