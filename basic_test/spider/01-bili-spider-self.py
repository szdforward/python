# -*- coding: UTF-8 -*-
# 文档在百度网盘有 本地的话在F:\python_resources\Python爬虫基础5天速成（2021全新合集）

import bs4 #网页解析，获取数据
import re  #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定url，获取网页数据
import xlwt #进行excel的操作
import sqlite3  #进行sqlite数据库操作
import random
def main():
    #1、爬取网页
    baseurl = "https://movie.douban.com/top250?start="
    getData(baseurl)
    #2、解析数据
    #3、保存数据

def getData(baseurl):
    datalist = []
    askURL(baseurl)
    # for i in range(0,10):
    #     url = baseurl +str(i*25)
    #     html = askURL(url)      #保存获取到的网页源码
    return datalist

def askURL(url):
    headers=[{"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    ,{"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    ,{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    ]
    header = random.choice(headers)
    request = urllib.request.Request(url=url,headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

if __name__ == "__main__":
    main()
    print("爬取数据完成!")

