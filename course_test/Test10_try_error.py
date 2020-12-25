# -*- coding: UTF-8 -*-

# file=None
# try:
#     file=open("F:/temp/test.txt")
#     print(file.readline())
# except IOError as result:
#     pass
#     print("文件读取异常！")
#     print(result)
# finally:
#     if(file != None):
#         file.close()

try:
    f=open("F:/temp/test.txt")
    try:
        while True:
            content=f.readline()
            if(len(content) == 0 ):
                break
            else:
                print(content)
    except IOError as error:
        print("读取文件异常！")
        print(error)
except Exception as result:
    print(result)