#coding=utf-8
"""
https://www.runoob.com/python3/python3-string.html 可以看下这个，格式化字符的也在里面
还有这个：https://www.runoob.com/python/att-string-format.html format格式化函数
"""

str = 'HellooWorld!'    #字符串在python中本质上是一个字符序列Seq
# print(str)        # 打印整个字符串
# print(str[0])      # 打印字符串第一个字母 H
# print(str[2:5])     # 打印第3到第5个字母,含首不含尾!!! llo
# print(str[::2])     # HloWrd  从首部打印到尾部 跨步长为2，即跨1步，跨2步 得到跨2步之后的值  默认步长为1
# print(str[2:])      # 打印从第3个字母到末尾 llooWorld!
# print(str * 2)      # 字符串重复2次 HellooWorld!HellooWorld!
# print(str + "TEST")  # 字符串拼接 HellooWorld!TEST  注意这里只有str类型的才可以使用“+”号  其他类型使用的话会报错
# print("nihao %s" %"lining") #nihao lining
# print("nihao %s , wo shi %s" %("lining","szd")) #nihao lining , wo shi szd
# print("need 3zifu%3s" %"ab") #need 3zifu ab  这里说的是至少3个字符 如果后面的字符多余3个话，是可以全都显示的  即不够给你补空格，多了就全显示
# print("看看这是多少个zifu-%3.5s" %"abcdefghi") #看看这是多少个zifu-abcde  这里3.5代表的含义是至少3个，最多5个
# print("1/3=%5f" %3.3333333333) # 1/3=3.333333  %f 代表保留5位小数
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10.856)) #我叫 小明 今年 10 岁!
# print('H' in "Hello") # True 成员运算符 H是否包含在Hello 字符串中
# print(3 in "123")  # 执行的话，会报错：TypeError: 'in <string>' requires string as left operand, not int  后面是字符串，但是你用int类型的来判断，就报错了

#===============字符串函数
str = 'HellooWorld!'    #字符串在python中本质上是一个字符序列Seq
# print(str.lstrip("He"))#llooWorld!  删除字符串最左侧的字符  注意，这并不会改变该字符串，本身字符串就是不变的
# print(str.rstrip("!"))# HellooWorld  删除字符串最右侧的字符
# print(str.__len__())#12 这个应该是占内存大小
# print(len(str))#12 字符串的长度
# print(str.count("o"))#3 字符o在字符串中出现了3次
# print(str.count("o",1,5))#1 字符o在下标1到下标4（含首不含尾，下标5不包含）之间出现了1次
# rfind方法： str.rfind(str, beg=0 end=len(string)) str 要查找的字符串  beg 开始查找的位置  end 结束查找的位置 默认为字符串的长度
# print(str.rfind("or"))#7 返回字符串最后一次出现的位置，如果没有匹配项则返回 -1


#使用格式化符号进行进制转换  多加入了一个#号，目的是在转换结果头部显示当前进制类型，如不需要，可将#号去除
num=10
# print("十六进制：%#x" %num)  # 格式化无符号十六进制数   十六进制：0xa
# print("八进制：%#o" %num) # 格式化无符号八进制数   八进制：0o12
# print("十六进制：%#X" %num) #  格式化无符号十六进制数（大写） 十六进制：0XA


#字符串的分隔还有partition()这种方式
# str_partition = str.partition("oo")
# print(str_partition,type(str_partition)) #('Hell', 'oo', 'World!') <class 'tuple'>   返回的是一个tuple元组类型
# #没有找到分割符'abc'，返回头、尾两个空元素的元组。
# str_partition1 = str.partition("a")
# print(str_partition1,type(str_partition1)) #('HellooWorld!', '', '') <class 'tuple'>

# 针对 Counter 的升级使用 获取字符串中数字出现的次数
#必须引用如下库
from collections import Counter
#定义两个字符串变量
Var1 = "1116122137143151617181920849510"
Var2 = "1987262819009787718192084951"
#以字典的形式，输出每个字符串中出现的字符及其数量  对得到的结果，可以根据字典的定义进行其他操作
# print (Counter(Var1),type(Counter(Var1))) #Counter({'1': 12, '2': 3, '6': 2, '3': 2, '7': 2, '4': 2, '5': 2, '8': 2, '9': 2, '0': 2})  <class 'collections.Counter'>
# print (Counter(Var2))#Counter({'1': 5, '9': 5, '8': 5, '7': 4, '2': 3, '0': 3, '6': 1, '4': 1, '5': 1})
# print (Counter(Var2)['1']) # 从字典中取出数字1出现的次数



#格式化输出字符串 Python字符串格式化 见https://www.runoob.com/python3/python3-string.html文档中也包含：f-string 是 python3.6 之后版本添加的 代表着格式化字符串
from string import Template
s =Template("There are ${howmany} ${lang} Quotation Symbols")
# print(s.substitute(lang='Python',howmany=3)) # There are 3 Python Quotation Symbols

##字符串 join
# print("##".join(("a","b"))) # 结果为： a##b

## 字符串正则匹配
import re
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
#    print("matchObj.group() : ", matchObj.group())
#    print("matchObj.group(1) : ", matchObj.group(1))
#    print("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print("No match!!")

#字符串与列表、元组的互相转换
var='菜鸟教程'
list=[]
list=[i for i in var]
# 字符串转化为元组，使用 tuple() 函数
tup=tuple(var)
# print(tup)


