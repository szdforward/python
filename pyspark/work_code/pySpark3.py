#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark import SparkContext
from pyspark.sql import SparkSession,HiveContext
import pyspark.sql.functions as F
import datetime as dt
from pyspark.sql.types import *
import json
#import pandas as pd
#import numpy as np

'''
当需要把Spark DataFrame转换成Pandas DataFrame时，可以调用toPandas()；
当需要从Pandas DataFrame创建Spark DataFrame时，可以采用createDataFrame(pandas_df)。
但是，需要注意的是，在调用这些操作之前，
需要首先把Spark的参数spark.sql.execution.arrow.enabled设置为true，
因为这个参数在默认情况下是false
'''

# 获取spark的上下文
sc = SparkContext('yarn', 'spark_file_conversion')
sc.setLogLevel('WARN')
spark_session = SparkSession.builder.getOrCreate()
spark_session.conf.set("spark.sql.execution.arrow.enabled", "true")
print("initialization success")
hive_context= HiveContext(spark_session)

# 生成查询的SQL语句，这个跟hive的查询语句一样，所以也可以加where等条件语句
hive_database = "da_market"
hive_table = "channel_cost_summary"
hive_read = "select distinct date_detail from {}.{}".format(hive_database,hive_table)
# 通过SQL语句在hive中查询的数据直接是dataframe的形式
read_df = hive_context.sql(hive_read)
# read_df.show()

def days_from_month(s):
    y = int(s.split("-")[0])
    m = int(s.split("-")[1])
    if m == 12:
        start_date = dt.datetime(year=y,month=m,day=1)
        end_date = dt.datetime(year=y+1,month=1,day=1)
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

udf_get_days_between = F.udf(get_days_between,ArrayType(StringType()))

#operation_col = read_df.select(read_df['courseid'],read_df['operation'])
read_df = read_df.withColumn("days", udf_get_days_between('date_detail'))
read_df = read_df.withColumn("divider", F.size('days'))

result = read_df.select(read_df['date_detail'],F.explode(read_df['days']),read_df['divider'])

result.show(5)

# 写入数据
file_name = "market_dates_mapping"
db_name = "dw_finance"

spark_session.sql("drop table if exists " + db_name+ "."+file_name)
result.write.options(header=True).mode("overwrite").saveAsTable(db_name+ "."+file_name)


