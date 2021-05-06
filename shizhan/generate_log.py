#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:generate_log.py
@time:2021/03/26
"""

import time
import random
from random_words import RandomWords
def gen(rank):
    # 先确认每个小时的查询数目，里面的数都是随机生成的，没有什么特殊含义
    query_nums = []
    for h in range(0, 6):
        query_nums.append(random.randint(1, 10) * rank) # 0点到6点的比较少
    for h in range(6, 12):
        query_nums.append(random.randint(h * 2, h * 3) * rank) # 6点到12点的逐渐增多
    for h in range(12, 24):
        query_nums.append(random.randint((24 - h) * 2, (24 - h) * 3) * rank) # 12点到24点逐渐减少
    print("每小时访问数"+str(query_nums))
    print("总访问数："+str(sum(query_nums)))
    rw = RandomWords() # 用于随机生成一个单词
    terminals = ["pc", "android", "iphone"] # 终端，可以分析维度
    zero_ts = time.mktime(time.strptime("2021-01-04 00:00:00", "%Y-%m-%d %H:%M:%S")) # 时间戳的起点
    res = []
    for hour in range(24):
        for cnt in range(0, query_nums[hour]): # 生成每小时的具体访问记录
            user_id = random.randint(50, 100)
            word = rw.random_word()
            terminal = terminals[random.randint(0, 2)]
            ts = str(int(zero_ts) + hour * 3600 + random.randint(0, 3600))
            res.append((str(user_id), word, terminal,ts))
    res.sort(key=lambda x: x[3]) # 按时间戳排序
    # 写入文件
    with open("./user_word.log", mode="w", encoding="utf-8") as f:
        for r in res:
            f.write(",".join(r) + "\n")
def check():
    # 查看生成数据的情况
    with open("./user_word.log", mode="r", encoding="utf-8") as f:
        for line in f:
            strs = line.split(",")
            dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(strs[3])))
            print(line.strip("\n")+","+dt)
if __name__ == '__main__':
    gen(10) # rank用来控制生成数据的量级,10大概是3.5k条，100大概是3.5w条
    check()
