#coding=utf-8

"""
文件的操作 遍历得到整个文件夹的大小
"""

import os
import re

def getFileSize(filePath,desc):
    # os.walk的用法：https://www.runoob.com/python/os-walk.html
    for root,dirs,files in os.walk(filePath):
        size=0
        for f in files:
            size += os.path.getsize(os.path.join(root,f))
        sizeM=size/1024/1024
        if sizeM > 100:
            desc.write('%s \t %2f\n'%(root,sizeM))
            # print(root,dirs,files,size/1024/1024,sep="\t")
    return

cpanfile=open("F:/temp/cpan.txt",'w')
getFileSize("C:/Users",cpanfile)
cpanfile.close
print("done")








