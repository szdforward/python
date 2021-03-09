#coding=utf-8
def func1(arg):
    print("in func1: %s" %arg)

def func2(arg):
    print("in func2: %s" %arg)

##函数名加下划线，别的地方使用import * 导入时，该函数默认不会导入
def _func3(arg):
    print("in func3: %s" %arg)


def func4(arg):
    print("in func4: %s" %arg)

# import os
# a=os.listdir("c:/")
# print(a)
# # os.makedirs("c:/pythontest/test")
# os.removedirs("c:/pythontest/test")
