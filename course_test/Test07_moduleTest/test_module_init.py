#coding=utf-8
"""
测试包中的__init__.py
"""

from course_test.Test07_moduleTest.moduletest.test1 import *
func1('haha')
func2('bibi')
# _func3("kkkkk")  #私有成员，导入不成功
func4("didi")

#显式导入
from course_test.Test07_moduleTest.moduletest.test1 import _func3
_func3("haha")

#还是没太搞懂这里 包里面的__init__.py文件内不清楚怎么使用-szd
#直接导入包
# import course_test.Test07_moduleTest.moduletest
# print(func4("aa"))