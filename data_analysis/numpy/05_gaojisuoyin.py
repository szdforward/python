
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:05_gaojisuoyin.py
@time:2021/03/12
"""
import numpy as  np
a = np.arange(12)**2
# print(a)#[  0   1   4   9  16  25  36  49  64  81 100 121]

x=np.array([[1,2],[3,4],[5,6]])
y=x[[0,1,2],[0,1,0]]
# print(y)#[1 4 5]

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
rows=np.array([[0,0],[3,3]])
cols=np.array([[0,2],[0,2]])
y=x[rows,cols]
# print(y)
# [[ 0  2]
#  [ 9 11]]

a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b=a[1:3,1:3]
# print(b)
# [[5 6]
#  [8 9]]
c=a[1:3,[1,2]]
# print(c)
# [[5 6]
#  [8 9]]
d=a[...,1:]
# print(d)
# [[2 3]
#  [5 6]
#  [8 9]]

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
# print(x[x>5])
# [ 6  7  8  9 10 11]
# 过滤掉NaN的数据
a = np.array([np.nan,1,2,np.nan,3,4,5])
# print(a[~np.isnan(a)])#[1. 2. 3. 4. 5.]
# 过滤出复数
a = np.array([1,  2+6j,  5,  3.5+5j])
# print(a[np.iscomplex(a)])
#[2. +6.j 3.5+5.j]

# 花式索引
x=np.arange(32).reshape((8,4))
# print(x[[4,2,1,7]])
# [[16 17 18 19]
#  [ 8  9 10 11]
#  [ 4  5  6  7]
#  [28 29 30 31]]

print(x[np.ix_([1,5,7,2],[0,3,1,2])])
# [[ 4  7  5  6]
#  [20 23 21 22]
#  [28 31 29 30]
#  [ 8 11  9 10]]

