#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:BitmapFunction.py
@time:2021/03/31
bitmap算法
"""

def clear(i,a):
    shift = i & 7 # 计算应该放在哪个位下 相当于i%8 除以8的余数
    arrindex = i >> 3 #计算应该放数组的下标，相当于i//8  取商
    bitPos = ~(1 << shift)
    a[arrindex] &= (bytes)(bitPos)


if __name__ == '__main__':
    clear(10,[12,23,45])
