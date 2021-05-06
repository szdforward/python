#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

# print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
# print( random.random() )             # 产生 0 到 1 之间的随机浮点数
# print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
# print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

# 将序列a中的元素顺序打乱
a=[1,3,5,6,7]
random.shuffle(a)
# print(a)

ua=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
    ,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36Chrome 17.0 – MAC"
    ,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    ]
# print(random.choice(ua))# randow.choice会从序列中随机挑选一个

# 随机整数：
# print(random.randint(1,50))

# 随机选取0到100间的偶数：
# print(random.randrange(0, 101, 2))

# 随机浮点数：
# print(random.random())
# print(random.uniform(1, 10))

# 随机取一个字符：
# print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))
# 随机取数
# print("随机取数",random.choice(range(100)))

import string
# 多个字符中生成指定数量的随机字符： 字符串不重复 如果多个字符串的数量小于要取的指定的数量，则会报错
print(random.sample('zyxwvutsrqponmlkjihgfedcba',5),type(random.sample('zyxwvutsrqponmlkjihgfedcba',5)))
print(random.sample(string.ascii_letters,4))

# 从a-zA-Z0-9生成指定数量的随机字符：
# ran_str = ''.join(random.sample(string.ascii_letters + str.digits, 8))
# print(ran_str)

# 多个字符中选取指定数量的字符组成新字符串：
# print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 随机选取字符串：
# print(random.choice(['剪刀', '石头', '布']))

# 打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)
# print(items)
