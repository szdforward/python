#encoding=utf-8

import requests
from bs4 import BeautifulSoup

# szd-不知道怎么用
res = requests.get('http://jandan.net/ooxx')
html = BeautifulSoup(res.text)
# print(html)

for index, each in enumerate(html.select('#comments img')):
    # print((index,each))
    imgurl = each.attrs['src']
    content = requests.get(imgurl).content
    f = open('{}.jpg'.format("g:/xxoo" + str(index)), 'wb')
    f.write(content)
    f.close()
