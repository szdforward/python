#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:冒泡排序.py
@time:2021/03/07
"""
def maopao(li):
    for ad in range(len(li)-1):
        for x in range(len(li)-ad-1):
            if (li[x]>li[x+1]):
                li[x+1],li[x]=li[x],li[x+1]
    return li
print(maopao([1,23,4,67,5,0,0]))