#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 匿名函数 可以使用lambda关键字来创建小的匿名函数。这些函数被称为匿名
# Lambda形式可以采取任何数量的参数，但在表现形式上只返回一个值。它们不能包含命令或多个表达式。
# lambda函数都有自己的命名空间，并且不能访问变量高于在其参数列表和那些在全局命名空间的变量
sum=lambda x,y:(x+1,y+1)
(a,b)=sum(2,3)
c=sum(2,3)
print(a,b) # 3 4
print(c[0],c[1]) # 3 4

# 函数中传递匿名函数
# 利用lambda可以实现类似于scala中的高阶函数效果
def outfunc(func,x,y):
    c=func(x,y)
    print(c)

outfunc(lambda x,y:x+y,1,2)


