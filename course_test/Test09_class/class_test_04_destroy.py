#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 类的创建和销毁 同Java语言一样，Python使用了引用计数这一简单技术来追踪内存中的对象

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   # __del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "销毁")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3)) # 打印对象的id 37917696 37917696 37917696  其实也就是把当前实例的地址给其他的对象
del pt1
print("pt1 later")
del pt2
print("pt2 later")
del pt3 #Point 销毁  在这一步 创建的对象实例会被销毁 因为已经没有引用了
print("pt3 later")