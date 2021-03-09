#-*- codeing = utf-8 -*-
#@Time : 2020/3/3 20:06
#@Author : 李巍
#@File : testUrllib.py
#@Software: PyCharm


import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码


#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode("utf-8"))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://www.baidu.com")
# #print(response.status) # 200
# print(response.getheader("Server"))#BWS/1.1



# url = "http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://movie.douban.com/top250?start="
# 下面的这个agent是我笔记本的  如果使用其他的user-agent的话，可以看下这个：https://blog.csdn.net/qq_44766315/article/details/107211158
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
req.add_header("Cookie","OUTFOX_SEARCH_USER_ID=-262674761@111.16.148.5; OUTFOX_SEARCH_USER_ID_NCOO=1237396375.7975602; _ga=GA1.2.500915091.1580871823; _ntes_nnid=5abb20c4601a7c520906e95569a5221e,1595132426933; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217700e87c092d8-0394f7bfa9bb61-5c19341b-1327104-17700e87c0a8a3%22%2C%22%24device_id%22%3A%2217700e87c092d8-0394f7bfa9bb61-5c19341b-1327104-17700e87c0a8a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; hb_MA-AF18-4208343217D0_source=bdms.inner.youdao.com; UM_distinctid=177c499288541f-024be90eb63433-5c19341b-144000-177c499288647b; JSESSIONID=87EBAFCD6D860014900E9F8E3E82AEE1; atlassian.xsrf.token=BQBK-N6CI-8220-7NVB_71d05d7ff1959e4bbc1f7661396ded79e0e6613a_lin")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

















