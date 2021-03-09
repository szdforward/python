#coding=UTF-8
"""
运算符的使用
"""
#=================算术运算符
#取模
# print(5%3)#2
#取幂
# print(2**4)#16
#取整除 向下取接近商的整数
# print(11//4)#2

#=================比较运算符
#  ==  !=  >  < >= <=

#=================赋值运算符
#  =  +=  -=
# := 海象运算符 可在表达式内部为变量赋值 python3.8新增的 见：https://www.runoob.com/python3/python3-basic-operators.html#ysf1  szd-运行不正确
# a=10
# if (n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expected <= 10)")

#=================逻辑运算符
# and or not  使用这三个逻辑运算符肯定是可以的  至于& | ^等，是位运算符
a,b=10,20
# if (a and b): #注意这里使用&这个符号是不行的   if (a & b):  不起作用
    # print("a和b这两个变量都为true") #a和b这两个变量都为true

#=================位运算符 & | ^ ~  << 等
print(98 & 97) # 96

#=================成员运算符
# in   not in

#=================身份运算符
# is   is not  类似于 == 和 != ,但是不等于 == 和 != ，例如在使用id()来做is运算的时候，有点不便于理解  还是使用== 和 != 吧  这种特殊的身份运算符用的会少一些
# is 与 == 区别：https://www.runoob.com/python3/python3-basic-operators.html#ysf1 这个连接里有介绍
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
a=b=10
c=d=345111
# print(a is b)#True
# print(c is d)#True
# print(id(a) == id(b))#True
# print(id(a) is id(b))#False
# print(id(c) == id(d))#True
# print(id(c) is id(d))#False