import random
from urllib import request
ua=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
    ,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36Chrome 17.0 – MAC"
    ,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    ]
headers={
    "User-Agent":random.choice(ua)
}
url="https://www.douban.com"
r=request.Request(url,headers=headers)
print(random.choice(ua))
r1=request.urlopen(r).read().decode("utf-8")
print(r1)
