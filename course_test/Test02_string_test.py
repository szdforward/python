#coding=utf-8

str = 'HellooWorld!'    #字符串在python中本质上是一个字符序列Seq

print(str)        # 打印整个字符串
print(str[0])      # 打印字符串第一个字母 H
print(str[2:5])     # 打印第3到第5个字母,含首不含尾!!! llo
print(str[2:])      # 打印从第3个字母到末尾 llooWorld!
print(str * 2)      # 字符串重复2次 HellooWorld!HellooWorld!
print(str + "TEST")  # 字符串拼接 HellooWorld!TEST  注意这里只有str类型的才可以使用“+”号  其他类型使用的话会报错

#格式化输出字符串 Python字符串格式化 见https://www.runoob.com/python3/python3-string.html文档中也包含：f-string 是 python3.6 之后版本添加的
sss ="Hello,%s,%s enough for ya?"
values =('world','Hot')
print(sss %values) # Hello,world,Hot enough for ya?  注意这里在sss后面加空格或者不加空格都是可以的

from string import Template
s =Template("There are ${howmany} ${lang} Quotation Symbols")
print(s.substitute(lang='Python',howmany=3)) # There are 3 Python Quotation Symbols

##字符串 join
print("##".join(("a","b"))) # 结果为： a##b

## 字符串正则匹配
import re
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")



