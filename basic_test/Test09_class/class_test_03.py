#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python的内置类属性

class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

emp01 = Employee("zhangsan",100000)
print(emp01.name)
print(emp01.salary)
emp01.displayCount() #Total Employee 1
emp01.displayEmployee()
attr = getattr(emp01,'age',None)
print(attr) #None

print("Employee.__doc__:", Employee.__doc__) #Employee.__doc__: 所有员工的基类
print("Employee.__name__:", Employee.__name__) #Employee.__name__: Employee
print("Employee.__module__:", Employee.__module__) #Employee.__module__: __main__
print("Employee.__bases__:", Employee.__bases__) #Employee.__bases__: (<class 'object'>,)
print("Employee.__dict__:", Employee.__dict__) #Employee.__dict__: {'__module__': '__main__', '__doc__': '所有员工的基类', 'empCount': 0, '__init__': <function Employee.__init__ at 0x00000000022150D0>, 'displayCount': <function Employee.displayCount at 0x0000000002215160>, 'displayEmployee': <function Employee.displayEmployee at 0x00000000022151F0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
