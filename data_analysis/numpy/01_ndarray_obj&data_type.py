#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:ndarray_obj.py
@time:2021/03/09
Ndarray对象和numpy的数据类型
"""

import numpy as np
#===============Ndarray对象
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object:数组或嵌套的数列   dtype:数组元素的数据类型，可选   copy:对象是否需要复制 可选   order:创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok:默认返回一个与基类类型一致的数组  ndmin:指定生成数组的最小维度
# 单维度
# a = np.array([1, 2, 3])
# print(a)
#多维度
# a = np.array([[1,2,3,4],[3,5,6,7]])
# print(a)
# print(a.shape)#(2, 4) 代表着2行4列
# 最小维度
# a=np.array([1,2,3,4,5],ndmin=3)
# print(a)#[[[1 2 3 4 5]]]  如果是4的话，代表4层嵌套数组了
# dtype参数
# a=np.array([1,2,3,4],dtype=complex)
# print(a)#[1.+0.j 2.+0.j 3.+0.j 4.+0.j]

# ==================numpy的数据类型dtype  一般有bool_ int_ intc int8 int16 uint32 uint64 float_ float32 float64 complex_ complex128等
# 字节顺序是通过对数据类型预先设定 < 或 > 来决定的。 < 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。> 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。
# dtype对象的构造 numpy.dtype(object,align,copy)
# object 要转换为的数据类型对象  align - 如果为 true，填充字段使其类似 C 的结构体  copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用
# dt1=np.dtype(np.int64)
# print(dt1)#int64
# dt2=np.dtype("i4")#字符串 i1 i2 i4 i8 分别对应：int8 int16 int32 int64
# print(dt2)#int32

# 结构化数据类型的使用
# 首先创建结构化数据类型
# dt3=np.dtype([('age',np.int8)])
# a=np.array([(10,),(20,),(30,)],dt3)
# print(a)#[(10,) (20,) (30,)]
# # 类型字段名可以用于存取实际的 age 列
# print(a['age'])#[10 20 30]
# 我们还可以定义一个结构化的数据类型student
student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
a=np.array([('abc',12,50),('xyz',32,75)],student)
print(a)#[(b'abc', 12, 50.) (b'xyz', 32, 75.)]





