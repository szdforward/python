#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print("调用父类构造函数")

   def parentMethod(self):
      print('调用父类方法')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("父类属性 :", Parent.parentAttr)

class Child(Parent): # 定义子类
   def __init__(self):
      print("调用子类构造方法")

   def childMethod(self):
      print('调用子类方法 child method')

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法

#class C(A, B):   # 继承类 A 和 B
# 可以使用issubclass()或者isinstance()方法来检测。
# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。