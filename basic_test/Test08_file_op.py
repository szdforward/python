#coding=utf-8

"""
文件的操作
"""
# import os
# files = os.listdir("F:\python_resources\day37-python\day37课件资料")
# logfile=[f for f in files if f.endswith('.exe') ]
# print(logfile) # ['Anaconda3-2.4.1-Windows-x86_64.exe', 'pycharm-community-5.0.2.exe', 'python-3.8.2.exe', 'python-3.8.5-amd64.exe']

# fileHandler = open('F:/temp/hello.py', 'a+')	#以读写方式处理文件IO 文件路径需要使用反斜杠
# fileHandler.seek(0)
# 读取一行
# line = fileHandler.readline()
# while line:
# 	print(line)
# 	line = fileHandler.readline()
# fileHandler.close


# fileHandler = open('F:/temp/hello.py', 'a+')	#以读写方式处理文件IO
# fileHandler.seek(0)
# #读取整个文件
# contents = fileHandler.read()
# print(contents,type(contents)) # print("hello world!") <class 'str'>
# #读取所有行,再逐行输出
# fileHandler.seek(0)
# lines = fileHandler.readlines()
# print(type(lines)) # <class 'list'>
# for line  in lines:
# 	print(line)
# #当前文件指针的位置
# print(fileHandler.tell()) # 21
# fileHandler.close


# 写入文件
fileHandler = open('F:/temp/hello.py','a+')   #或者调用open()函数
fileHandler.write("\r\n")
fileHandler.write("thank you")
fileHandler.seek(0)
contents = fileHandler.read()
print(contents)
fileHandler.close

