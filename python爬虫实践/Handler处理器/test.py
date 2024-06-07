import urllib.request
import urllib.parse
url = 'https://www.zhihu.com/'
headers = {"User-Agent" :
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}

request = urllib.request.Request(url=url,headers=headers)

# handler = urllib.request.HTTPHandler()
# opener = urllib.request.build_opener(handler)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

with open('zhihu.html','w',encoding='utf8') as fp:
    fp.write(content)

