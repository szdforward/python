# -*- coding: UTF-8 -*-
"""
复制一个文件到另一个文件
新建一个gushi.txt的文件，并写入文字
复制gushi.txt为copy.txt
"""
import os
import random

#此函数跟hadoop fs -cp的使用方法类似
def copyFile(origin,des):
    originDirName=os.path.dirname(origin)
    originBaseName=os.path.basename(origin) # 代表文件的名字 例如如果origin为：F:/temp/copy.txt 则得到的结果为：copy.txt
    #查看目标路径是否存在，如果不存在则创建
    desDirName=os.path.dirname(des)
    if(not(os.path.exists(desDirName))):
        os.makedirs(desDirName)
    #看目标是否传入了文件名，如果没有文件名的话:如果目标路径相同，则使用不同的文件名，如果路径不相同，则使用复制文件的文件名
    desBaseName=os.path.basename(des)
    if(desBaseName == ""):
        if(originDirName == desDirName ):
            desBaseName=originBaseName+str(random.random())
        else:
            desBaseName=originBaseName
    try:
        originFile=open(origin)
        desFile=open(desDirName+"/"+desBaseName,"w")
        line=originFile.readline()
        while line:
            desFile.write(line)
            line=originFile.readline()
        print("复制成功！")
    except Exception as result:
        print(result)

f=open("F:/temp/gushi.txt","w")
f.write("白日依山尽\n")
f.write("黄河入海流\n")
f.write("欲穷千里目\n")
f.write("更上一层楼\n")
f.flush()
f.close()
copyFile("F:/temp/gushi.txt","F:/temp/copy.txt")
