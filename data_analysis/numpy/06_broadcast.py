#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:06_broadcast.py
@time:2021/03/15
"""
import numpy as  np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
# print(a*b)#[ 10  40  90 160]

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
# print(a*b)
# [[ 0  0  0]
#  [10 20 30]
#  [20 40 60]
#  [30 60 90]]

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
np.tile(b,(4,1))#行数上重复4次
# print(a+b)
# [[ 1  2  3]
#  [11 12 13]
#  [21 22 23]
#  [31 32 33]]
