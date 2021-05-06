#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:Test15_system.py
@time:2021/03/27
"""

import os,sys

name0 = sys.argv[0] # 指的是该python文件的绝对路径：
print(name0,type(name0))# E:/python_resources/day37-python/day37课件资料/代码/PycharmProjects/basic_test/Test15_system.py <class 'str'>
name1 = sys.argv[0].rfind(os.sep)+1
print(name1)# 0
name2 = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
print(name2)# E:/python_resources/day37-python/day37课件资料/代码/PycharmProjects/basic_test/Test15_system_os.py
name3 = name2.rstrip('.py')
print(name3)# E:/python_resources/day37-python/day37课件资料/代码/PycharmProjects/basic_test/Test15_system_os

# os.sep 的解释：https://blog.csdn.net/qq_18483627/article/details/105365191
print(os.sep)# \

