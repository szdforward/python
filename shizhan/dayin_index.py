#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:dayin_index.py
@time:2021/03/16
输入不同的数组后打印多维数组的下标
"""
import numpy as np

# nparr=np.array([1, 2,3,4])
# nparr=np.array([[1, 2,3,4], [3, 4, 5,6], [6, 7, 8, 9]])
# nparr=np.array([[[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]]])
nparr=np.arange(120).reshape(2,3,4,5)
print(nparr)
# 秩
zhi=nparr.ndim
tuple1=nparr.shape
# 递归函数
def digui(ceng,tuple1,zhi,list1):
    zhi -= 1
    for index in range(tuple1[ceng]):
        list1[ceng]=index
        if(zhi > 0):
            digui(ceng+1,tuple1,zhi,list1)
        else:
            print('(',str(list1).strip("[]"),')',nparr[tuple(list1)])

list1 = [0 for i in range(len(tuple1))]
digui(0,tuple1,zhi,list1)
