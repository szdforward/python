# coding=utf-8
# 类型转换

# x='ff'
# y=int(x,16) #int(x [,base]) 将x转换为整数。基数指定为base（进制） 即x代表的是base进制的数字  例如如果你写16进制的话，x就必须为16进制的表达式  例如ff等
# print(y,type(y)) # 256 <class 'int'>

# 进制转换
# x=10
# y=hex(x) # 返回十六进制
# z=oct(x) # 返回八进制
# print(y,type(y)) # 0xa <class 'str'>
# print(z,type(z)) # 0o12 <class 'str'>
# print(int(y,16)) # 10

# x='1.0'
# print(x,type(x),id(x)) # 1.0 <class 'str'> 34753968
# y=float(x)
# print(y,type(y),id(y)) # 1.0 <class 'float'> 34559952

# x=1
# y=complex(x,10) # complex(real [,imag])  创建一个复数
# print(x,type(x)) # 1 <class 'int'>
# print(y,type(y)) # (1+10j) <class 'complex'>


# x=[1,2,3,4]
# y=str(x)
# print(x,type(x)) # [1, 2, 3, 4] <class 'list'>
# print(y,type(y)) # [1, 2, 3, 4] <class 'str'>


# x='1+2'
# y=repr(x) # repr(x)  返回对象的标准字符串
# z=eval(y) # eval(str)  计算一个表达式字符串，并返回一个对象
# zz=eval(x)
# print(x,type(x)) # 1+2 <class 'str'>
# print(y,type(y)) # '1+2' <class 'str'>
# print(z,type(z)) # 1+2 <class 'str'>
# print(zz,type(zz)) # 3 <class 'int'>


# x='angelababy'  #字符串属于序列
# y=tuple(x)
# z=list(x)
# print(x,type(x),id(x)) # angelababy <class 'str'> 39210288
# print(y,type(y),id(y)) # ('a', 'n', 'g', 'e', 'l', 'a', 'b', 'a', 'b', 'y') <class 'tuple'> 4124480
# print(z,type(z),id(z)) # ['a', 'n', 'g', 'e', 'l', 'a', 'b', 'a', 'b', 'y'] <class 'list'> 39210880
# a=tuple(range(1,10,2))
# print(a) #(1, 3, 5, 7, 9)

# x=97
# y=chr(x)    #整型转对应的字符
# o=ord('a')
# print(y,type(y)) # a <class 'str'>
# print(o,type(o)) # 97 <class 'int'>



f=dict([(1,2),(3,4),('a',100)])
print(f.keys()) #dict_keys([1, 3, 'a'])
print(f.values()) #dict_values([2, 4, 100])
print(f[1],f[3]) #打印key为1和key为3对应的value： 2 4
print(f) #{1: 2, 3: 4, 'a': 100}




