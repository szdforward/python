#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:04_slice_and_other.py
@time:2021/03/10
"""
import numpy as np

# 1、从已有的数组创建数组
# np.asarray(a,dtype,order) a:任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组  dtype:数据类型，可选  order:可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
# 将数组转为ndarray
a=np.asarray([1,2,3])
# print(a)#[1 2 3]
# 将元祖转为ndarry
b=np.asarray((1,2,3,4))
# print(b)#[1 2 3 4]
# 将元祖列表转为ndarray # 这种不等长的列表已经过期了 不建议使用了
c=np.asarray([(1,2,3),(4,5)])
# print(c)#[(1, 2, 3) (4, 5)]
# 设置dtype参数类型
d=np.asarray([1,2,3,4],dtype=float)
# print(d)#[1. 2. 3. 4.]

#2、numpy.frombuffer 用于实现动态数组
#buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。
e=np.frombuffer(b'Hello World!',dtype='S1')
# print(e)#[b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd' b'!']

#3、numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
li1=range(5)
it1=iter(li1)
f=np.fromiter(it1,dtype=float)
# print(f)#[0. 1. 2. 3. 4.]

#4、从数值范围创建数组 numpy.arange(start, stop, step, dtype)
#生成 0 到 5 的数组:
# print(np.arange(5,dtype=float))#[0. 1. 2. 3. 4.]
# 设置起始值、终止值及步长
# print(np.arange(10,20,2))#[10 12 14 16 18]

#5、numpy.linspace 创建等差数列  函数用于创建一个一维数组，数组是一个等差数列构成的
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)  num代表：要生成的等步长的样本的数量
a=np.linspace(2,20,5,endpoint=True,retstep=True,dtype=float)
# print(a)#(array([ 2. ,  6.5, 11. , 15.5, 20. ]), 4.5)
# 设置等差数列后，可以reshape调整维度
b=np.linspace(3,30,6,dtype=float).reshape([3,2])
# print(b)
# [[ 3.   8.4]
#  [13.8 19.2]
#  [24.6 30. ]]

# 6、创建一个等比数列 numpy.logspace 函数用于创建一个于等比数列
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None) start 序列的起始值为：base ** start  base:对数 log 的底数。base 参数意思是取对数的时候 log 的下标。
h=np.logspace(0,9,base=2,num=10)#num 默认是50
print(h)#[  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]


# 对已有的数组进行切片
a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
# print (a[s])#[2 4 6]
# print(a[2:7:2])#[2 4 6]

