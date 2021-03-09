#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:count2jinzhi1deGeShu.py
@time:2021/03/06
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

# 方法1：
def NumberOf1(n):
    # write code here
    cnt = 0
    if n < 0:  # 如果是负数的话，取补码
        n = n & 0xffffffff
    while n:
        cnt += 1
        n = (n - 1) & n # 代码说明见onenote上的 位运算
    return cnt

# bin函数： bin返回一个整数的二进制字符串，以0b开头，
    # bin(10) '0b1010'  bin(-10)  '-0b1010'
# count函数 返回字符串当中非重叠的字符串的个数，可以传入start，end来表示对字符串切片的结果
# 方法2
def NumberOf1_2(n):
    if (n>=0):
        return bin(n).count("1")
    else:
        return bin(n & 0xffffffff).count("1")

if __name__ == '__main__':
    print(NumberOf1(98))#3
    # print([bin(num) for num in range(1, 99)])
    # print(bin(63))#0b111111
    print(NumberOf1_2(98))
    print(NumberOf1(1002))
    print(NumberOf1_2(1002))
    print(NumberOf1(-231002))
    print(NumberOf1_2(-231002))
