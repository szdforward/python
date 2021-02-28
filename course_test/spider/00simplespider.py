import requests
# 如果导入requests报错的话，可以安装包：python -m pip install requests
from bs4 import BeautifulSoup

# 一个简单的爬虫 szd-不清楚怎么用
res = requests.get('http://jandan.net/ooxx')
html = BeautifulSoup(res.text)
for index, each in enumerate(html.select('#comments img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        jpg.write(requests.get(each.attrs['src'], stream=True).content)