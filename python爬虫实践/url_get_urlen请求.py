import urllib.request
import urllib.parse
# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

#获取网页源码
# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE%E7%9C%81

baseurl = 'https://www.bing.com/search?q='
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
data_encoded = urllib.parse.urlencode(data)
url = baseurl + data_encoded
headers = {"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}

request = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(request)
src = res.read().decode('utf-8')
print(src)





