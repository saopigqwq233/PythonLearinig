import urllib.request
import urllib.parse
url = 'https://weibo.com/login.php?url=https%3A%2F%2Fwww.weibo.com%2F%3Fsudaref%3Dwww.bing.com%26display%3D0%26retcode%3D6102&sudaref=login.sina.com.cn&display=0&retcode=6102#_loginLayer_1697092764077'
headers = {"User-Agent" :
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
           }
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('gbk')

with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)


