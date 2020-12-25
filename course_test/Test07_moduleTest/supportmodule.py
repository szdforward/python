# coding=utf-8

#导入模块
import course_test.Test07_moduleTest.support
# 使用导入的模块中的函数
course_test.Test07_moduleTest.support.print_func("Zara")

#------------------------------------------------
#或者
from course_test.Test07_moduleTest.support import print_func

print_func("Zara")


###从任意路径引入
import sys
import os

print(sys.path)
print(os.path) # <module 'ntpath' from 'G:\\software\\Python38\\lib\\ntpath.py'>
workpath = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.insert(0, os.path.join(workpath, 'x:\\other'))
print(sys.path)# ['x:\\other', 'F:\\python_resources\\day37-python\\day37课件资料\\代码\\PycharmProjects\\course_test\\Test07_moduleTest', 'F:\\python_resources\\day37-python\\day37课件资料\\代码\\PycharmProjects', 'G:\\software\\Python38\\python38.zip', 'G:\\software\\Python38\\DLLs', 'G:\\software\\Python38\\lib', 'G:\\software\\Python38', 'G:\\software\\Python38\\lib\\site-packages']
# import othermodule
# print(othermodule.sum(1,2))