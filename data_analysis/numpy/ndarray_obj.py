#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:ndarray_obj.py
@time:2021/03/09
"""

import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object:数组或嵌套的数列   dtype:数组元素的数据类型，可选   copy:对象是否需要复制 可选   order:创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok:默认返回一个与基类类型一致的数组  ndmin:指定生成数组的最小维度
# 单维度
a = np.array([1, 2, 3])
# print(a)
#多维度
a = np.array([[1,2,3,4],[3,5,6,7]])
print(a)
print(a.shape)#(2, 4) 代表着2行4列
