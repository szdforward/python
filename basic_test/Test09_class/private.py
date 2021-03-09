#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 私有变量

class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print counter.__secretCount  # 报错，实例不能访问私有变量
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性：
print(counter._JustCounter__secretCount)