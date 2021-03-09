# coding=utf-8

# 基本使用
counter = 100  # 整型
miles = 1000.0  # 浮点
name = "John"  # 字符串

# print(counter, type(counter))
# print(miles, type(miles))
# print(name, type(name))

# 输入进制数 2进制是0b开头 8进制是0o开头  16进制是0x开头
jinzhi2 = 0b111
jinzhi8 = 0o11
jinzhi16 = 0x110
print(jinzhi2,jinzhi8,jinzhi16) # 这里会自动的打印出10进制的数  60 9 272
# #如果想打印出二进制、八进制、十六进制的数的话；可以使用bin oct hex 或者使用字符串的%x %o来格式化输出
# print(bin(jinzhi2),oct(jinzhi8),hex(jinzhi16),type(hex(jinzhi16)))#0b111100 0o11 0x110 <class 'str'>  注意oct hex等得到的结果为 str类型的
# print(0xffffffff)#4294967295
# 将16进制的数转换成2进制
# print(bin(0xffffffff))#0b11111111111111111111111111111111
# 将十进制的数转化成二进制
print(bin(18692))
print(bin(18693))


# 多重赋值
a = b = c = 1
d, e, f = 1, 2, "john"

a = 1
del a
# print(a)   #删除a变量后，再调用a变量会报错

# 进制转换
# x=10
# y=hex(x) # 返回十六进制
# z=oct(x) # 返回八进制
# print(y,type(y)) # 0xa <class 'str'>
# print(z,type(z)) # 0o12 <class 'str'>
# print(int(y,16)) # 10

# 创建复数
# x=1
# y=complex(x,10) # complex(real [,imag])  创建一个复数
# print(x,type(x)) # 1 <class 'int'>
# print(y,type(y)) # (1+10j) <class 'complex'>

# input的使用 让用户输入值
# print('----欢迎使用BMI计算程序----')
# name=input('请键入您的姓名:')
# height=eval(input('请键入您的身高(m):'))
