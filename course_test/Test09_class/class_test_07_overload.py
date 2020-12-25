#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Ventor:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'Ventor(%d,%d)'%(self.a,self.b)

    def __add__(self, other):
        return Ventor(self.a+other.a,self.b+other.b)

v1=Ventor(1,2)
v2=Ventor(2,6)
print(v1+v2) # Ventor(3,8)