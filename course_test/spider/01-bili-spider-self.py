# -*- coding: UTF-8 -*-
# 文档在百度网盘有 本地的话在F:\python_resources\Python爬虫基础5天速成（2021全新合集）

import bs4 #网页解析，获取数据
import re  #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定url，获取网页数据
import xlwt #进行excel的操作
import sqlite3  #进行sqlite数据库操作
def main():
    #1、爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    getData(baseurl)
    #2、解析数据
    #3、保存数据

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl +str(i*25)
        html = askURL(url)      #保存获取到的网页源码
    return datalist

def askURL(url):
    print("")

if __name__ == "__main__":
    main()
    print("爬取数据完成!")

