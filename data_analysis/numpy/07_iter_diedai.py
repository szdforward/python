#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:07_iter_diedai.py
@time:2021/03/15
迭代数组
"""

import numpy as np

a=np.arange(6).reshape(2,3)
for x in np.nditer(a):
    pass
    # print(x,end=",")
# 0,1,2,3,4,5,

for x in np.nditer(a.T):
    pass
    # print(x,end=",")
    # 0,1,2,3,4,5,

for x in np.nditer(a.T.copy(order="C")):
    pass
    # print(x,end=",")
# 0,3,1,4,2,5,

a = np.arange(0,60,5)
a = a.reshape(3,4)
# print(a)
# [[ 0  5 10 15]
#  [20 25 30 35]
#  [40 45 50 55]]
b=a.T#原始数组转置
# print(b)
# [[ 0 20 40]
#  [ 5 25 45]
#  [10 30 50]
#  [15 35 55]]
c=b.copy(order="C")
for x in np.nditer(c):
    pass
    # print(x,end=",")
    # 0,20,40,5,25,45,10,30,50,15,35,55,
# print("\n")
d=b.copy(order="F")
for x in np.nditer(d):
    pass
    # print(x,end=",")
    # 0,5,10,15,20,25,30,35,40,45,50,55,

#修改数组中元素的值
a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a,op_flags=["readwrite"]):
    x[...]=2*x
# print(a)
# [[  0  10  20  30]
#  [ 40  50  60  70]
#  [ 80  90 100 110]]

a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a,flags=["external_loop"],order='F'):
    pass
    # print(x,end=",")
# [ 0 20 40],[ 5 25 45],[10 30 50],[15 35 55],

# 广播迭代
a = np.arange(0,60,5)
a = a.reshape(3,4)
b=np.array([1,2,3,4],dtype=int)
for x,y in np.nditer([a,b]):
    pass
    # print("%d:%d" %(x,y),end=",")
# 0:1,5:2,10:3,15:4,20:1,25:2,30:3,35:4,40:1,45:2,50:3,55:4,
