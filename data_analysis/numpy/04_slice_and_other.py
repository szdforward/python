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
# print(h)#[  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]


# 对已有的数组进行切片
a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
# print (a[s])#[2 4 6]
# print(a[2:7:2])#[2 4 6]

#切割
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[2:])#[[7 8 9]]  从第2个开始切割出来（起始位置为0）

# 省略号的使用
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print (a[...,1])   # 第2列元素 #[2 4 5]
# print (a[1,...])   # 第2行元素 #[3 4 5]
# print (a[...,1:])  # 第2列及剩下的所有元素
# [[2 3]
#  [4 5]
#  [5 6]]

# 冒号 : 的解释：如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。如果为 [2:]，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
#在多维数组的切片中，使用 , 区分维数。在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）
a=np.arange(0,12)
a.shape=(3,4)
# print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# print(a[0:2,1:3])#可以理解为维度的话取0 1（包前不包后），使用逗号区分维度，再降一个维度，取 1:3 包前不包后，就是1 2 和 5 6了4
# [[1 2]
#  [5 6]]

#切片向量既可以为array,也可以为list类型  见：https://www.runoob.com/numpy/numpy-indexing-and-slicing.html
b = np.arange(0, 25)
b.shape = (5, 5)
print(b)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
r = np.array([0,1,4])  #r = [0,1,4]
c = [1, 2, 4]          #c = np.array([1,2,4])

#b[r,:]和b[r]得到的结果是一样的：
print(b[r,:])
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [20 21 22 23 24]]
print(b[r])
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [20 21 22 23 24]]

# e=[2,3]
# print("b[r][e]:\n",b[r][e])#这样执行的话会报错的：IndexError: index 3 is out of bounds for axis 0 with size 3  因为只有3组数组，但是你要取下标为2和下标为3的，下标为3是不存在的

e=[2]
print("b[r][e]:\n",b[r][e])
 # [[20 21 22 23 24]]

#注意b[r][2,3]和b[r][e] 这两个的含义是不同的： [2,3] 代表第一个维度取下标2，第二个维度取下标3 ； [e] 代表第一个维度取下标为(e这个数组中的元素)这些的下标数组
print("b[r][2,3]:\n",b[r][2,3])
# b[r][2,3]:
#  23

print("b[r][2,3:5]:\n",b[r][2,3:5])
# b[r][2,3:5]:
#  [23 24]


print("b_slice:\n", b[r, :][:, c])
 # [[ 1  2  4]
 # [ 6  7  9]
 # [21 22 24]]


#索引会改变维度  切片不会改变维度  像a[1] 是索引  a[1:2]这种是切片
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1],'\n',a[1,1])#[4 5 6]    5
print(a[1].ndim,a[1,1].ndim)# 1 0
print(a[1:],'\n',a[1:2,2:3])
# [[4 5 6]
#  [7 8 9]]
# 和
#  [[6]]
print(a[1:].ndim,a[1:2,2:3].ndim)#2 2
print(a[1:2])#[[4 5 6]]
