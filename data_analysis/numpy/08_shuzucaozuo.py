#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:08_shuzucaozuo.py
@time:2021/03/15
数组操作
"""
import numpy as np
a = np.arange(8)
a=a.reshape(2,4)
# print(a)
# [[0 1 2 3]
#  [4 5 6 7]]

# flat的使用 #对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
for x in a.flat:
    # print(x,end=",")
    # 0,1,2,3,4,5,6,7,
    pass

# flatten的使用 返回一组数组拷贝，不会影响到原始数组
a = np.arange(8).reshape(2,4)
# print(a.flatten())
# [0 1 2 3 4 5 6 7]
# print(a.flatten(order="F"))
# [0 4 1 5 2 6 3 7]

# ravel的使用
a = np.arange(8).reshape(2,4)
# print ('原数组：')
# print (a)
# print(a.ravel())
# 原数组：
# [[0 1 2 3]
#  [4 5 6 7]]
# [0 1 2 3 4 5 6 7]

