import urllib.request
import urllib.parse
# post请求
url = 'https://fanyi.baidu.com/sug'
headers = {"User-Agent" :
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
data = {
    'kw':'beautiful'
}

# post请求的参数必须编码
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url,data=data, headers=headers)

res = urllib.request.urlopen(request)

src = res.read().decode('utf-8')


#src是一个字符串
import json
obj = json.loads(src)
print(obj)




