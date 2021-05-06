#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:斐波纳契数列和print的使用.py
@time:2021/03/07
"""

# end 关键字：关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a,b,c=0,1,3
# print(a,end=",")
while b<100:
    # print(b,end=",")
    a,b=b,a+b

# seq关键字的使用
# print(a,b,c,sep="%") #89%144%3

list1=[1,2,3,4]
print(list1,sep=':')#[1, 2, 3, 4]
