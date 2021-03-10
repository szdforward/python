#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:02_shuzushuxing.py
@time:2021/03/09
numpy数组的一些基本属性
"""
import numpy as np

# a=np.array([[1,2,3,4,5],['a','b','c','d','e']])
# print(a)
# # [['1' '2' '3' '4' '5']
# #  ['a' 'b' 'c' 'd' 'e']]
# # 轴 每一个线性的数组称为是一个轴，也就是维度 axis axis=0 意味着第0轴，表示沿着第0轴进行操作，即对每一列进行操作；axis=1表示对第一轴进行操作，即对每一行进行操作
# # 秩 就是轴的数量
# # 比较重要的属性有：
# print(a.ndim)#2 秩
# print(a.size)#10 数组元素的总个数 相当于n*m
# print(a.dtype)# <U11   U代表：Unicode

#===================itemsize
# print(a.itemsize)#44 对象中每个元素的大小，以字节为单位 例如：一个元素类型为 float64 的数组 itemsize 属性值为 8(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节），又如，一个元素类型为 complex32 的数组 item 属性为 4（32/8）
# 数组的 dtype 为 int8（一个字节）
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)#1
# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1,2,3,4,5], dtype = np.float64)
print (y.itemsize)#8

# print(a.flags)#对象的内存信息
#   #C_CONTIGUOUS : True
#   # F_CONTIGUOUS : False
#   # OWNDATA : True
#   # WRITEABLE : True #数据区域可以被写入，将该值设置为 False，则数据为只读
#   # ALIGNED : True #数据和所有元素都适当地对齐到硬件上
#   # WRITEBACKIFCOPY : False
#   # UPDATEIFCOPY : False  #	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
# print(a.real)#元素的实部
# # [['1' '2' '3' '4' '5']
# #  ['a' 'b' 'c' 'd' 'e']]
# print(a.imag)#元素的虚部
# # [['' '' '' '' '']
# #  ['' '' '' '' '']]

#============shape 表示数组的维度，对于矩阵的话，n行m列  shape也可以用于调整数组大小  或者使用reshape函数来调整数组的大小
# ndarray.reshape 通常返回的是非拷贝副本，即改变返回后数组的元素，原数组对应元素的值也会改变
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)#(2, 3)
a.shape=(3,2)
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]
a=a.reshape(2,3)#注意，这里使用了reshape之后需要重新赋值给a 只是做reshage操作的话，改变不了a的
print(a)
# [[1 2 3]
#  [4 5 6]]
