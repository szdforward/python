# coding:utf-8
import sys,importlib
importlib.reload(sys)
sys.setdefaultencoding('utf8')
import re
import time
import json
import PyMySQL
import datetime
import subprocess
def cal_task_count(cursor, cur_day):
    def count_jenkins_task(cur_day, task_name):
        res = subprocess.Popen("sh ~/xiejiajun/cal_overtime/count_task_number.sh " + task_name, shell=True, stdout=subprocess.PIPE)
        res_str = res.stdout.read().strip('\n')
        return int(res_str)
    def count_azk_flow_task(cur_day, task_name):
        azk_db = PyMySQL.connect("analysis-db", "azkaban_secure", "azkaban_secure", "azkaban_secure", charset='utf8')
        azk_cursor = azk_db.cursor()
        azk_cursor.execute("SELECT COUNT(job_id) FROM execution_jobs WHERE flow_id LIKE 'FINAL_{}_{}_%';".format(cur_day, task_name))
        azk_result = azk_cursor.fetchone()
        return int(azk_result[0])
    cursor.execute("SELECT * FROM tb_task")
    task_results = cursor.fetchall()
    product_task_count_dict={}
    for row in task_results:
        product_name = row[1]
        task_name = row[2]
        task_url = row[3]
        task_type = row[4].encode("utf-8")
        task_info_list = []
        if task_type == 'jenkins':
            product_task_count_dict[product_name] = product_task_count_dict.get(product_name, 0) + count_jenkins_task(cur_day, task_name)
        elif task_type == "azkaban_flow":
            product_task_count_dict[product_name] = product_task_count_dict.get(product_name, 0) + count_azk_flow_task(cur_day, task_name)
        else:
            product_task_count_dict[product_name] = product_task_count_dict.get(product_name, 0) + 1
    return product_task_count_dict
def cal_late_mins(cursor, cur_cal_month, product_task_count_dict):
    holiday_list = []
    workday_list = []
    def judge_holiday(cur_day):
        time.sleep(2)
        try:
            if cur_day in workday_list:
                return False
            elif cur_day in holiday_list:       
                return True
            else:     
                res = subprocess.Popen("curl http://tool.bitefu.net/jiari/?d=" + cur_day, shell=True, stdout=subprocess.PIPE) # use others api,maybe fail
                res_str = res.stdout.read().strip('\n')
                if res_str != "0":
                    holiday_list.append(cur_day)
                    return True
                else:
                    workday_list.append(cur_day)
                    return False
        except:
            cur_week_day = datetime.datetime.strptime(cur_day, "%Y-%m-%d").isoweekday()
            return cur_week_day == 6 or cur_week_day == 7
    cursor.execute("SELECT product_name,etl_day,MAX(late_mins) FROM tb_task_daily_info WHERE etl_day like '{}%' AND task_status='SUCCESS' GROUP BY product_name,etl_day;".format(cur_cal_month))
    nature_day_late_mins_dict = {}
    work_day_late_mins_dict = {}
    late_mins_results = cursor.fetchall()
    for row in late_mins_results:
        product_name = row[0]
        etl_day = row[1]
        max_late_mins = float(row[2])
        nature_day_late_mins_dict[product_name] = nature_day_late_mins_dict.get(product_name, 0) + max_late_mins
        if not judge_holiday(etl_day):
            work_day_late_mins_dict[product_name] = work_day_late_mins_dict.get(product_name, 0) + max_late_mins
    for k,v in nature_day_late_mins_dict.items():
        task_count = product_task_count_dict[k]
        work_day_late_mins = work_day_late_mins_dict.get(k, 0)
        insert_sql = "INSERT INTO tb_task_month_info (product_name, etl_year_month, task_count, work_day_late_mins, natural_day_late_mins) VALUES ('{}', '{}', {}, {}, {});".format(k, cur_cal_month, task_count, work_day_late_mins, v)
        cursor.execute(insert_sql)
        print(insert_sql)
def cal_chain_ratio(cursor, cur_cal_month, day_type):
    last_cal_month = get_last_month(cur_cal_month)
    cursor.execute("SELECT product_name,{}_day_late_mins FROM tb_task_month_info WHERE etl_year_month='{}';".format(day_type, cur_cal_month))
    day_cur_month_dict=dict(cursor.fetchall())
    last_month = get_last_month(cur_month)
    cursor.execute("SELECT product_name,{}_day_late_mins FROM tb_task_month_info WHERE etl_year_month='{}';".format(day_type, last_cal_month))
    day_last_month_dict=dict(cursor.fetchall())
    for k,v in day_cur_month_dict.items():
        if k in day_last_month_dict.keys():
            last_late_mins = day_last_month_dict[k]
            chain_ration = int((v-last_late_mins)/last_late_mins*100)
            update_sql = "UPDATE tb_task_month_info SET {}_day_chain_ratio = '{}%' WHERE product_name = '{}' AND etl_year_month = '{}';".format(day_type, chain_ration, k, cur_cal_month)
            cursor.execute(update_sql)
            print(update_sql)
def get_last_month(cur_month):
    cur_month_day = datetime.datetime.strptime(cur_month, '%Y-%m')
    last_month_first = cur_month_day.replace(day=1)
    last_month = last_month_first - datetime.timedelta(days=1)
    return last_month.strftime("%Y-%m")

if __name__ == '__main__':
    cur_day = sys.argv[1]
    cur_month = cur_day[0:7]
    last_month = get_last_month(cur_month)
    db = PyMySQL.connect("10.109.13.132", "root", "iamroot", "db_calculate_overtime", charset='utf8')
    cursor = db.cursor()
    # calculate task_count and late_mins in order to insert
    product_task_count_dict = cal_task_count(cursor, cur_day)
    cal_late_mins(cursor, last_month, product_task_count_dict)
    db.commit()
    time.sleep(1)
    # calculate chain_ratio in order to update
    cal_chain_ratio(cursor, last_month, 'work')
    cal_chain_ratio(cursor, last_month, 'natural')
    db.commit()
    db.close()

