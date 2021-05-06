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

#转置
a = np.arange(12).reshape(3,4)
# print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# print(a.T)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

#rollaxis 向后滚动特定的轴到一个特定的位置  创建了一个三轴的ndarry numpy.rollaxis(arr, axis, start) arr：数组 axis：要向后滚动的轴，其它轴的相对位置不会改变  start：默认为零，表示完整的滚动。会滚动到特定位置。
a=np.arange(8).reshape(2,2,2)
# print(a)
# [[[0 1]
#   [2 3]]
#
#  [[4 5]
#   [6 7]]]
#获取原数组中的一个值
# print(np.where(a==6))#(array([1], dtype=int64), array([1], dtype=int64), array([0], dtype=int64))
# print(a[1,1,0])#6

# 将轴 2 滚动到轴 0（宽度到深度）
b = np.rollaxis(a,2,0)
# print(b)
# [[[0 2]
#   [4 6]]
#
#  [[1 3]
#   [5 7]]]
# print(np.where(b==6))
# print(b[1,1,0])

a = np.ones((3,4,5,6))
print(a.shape)
