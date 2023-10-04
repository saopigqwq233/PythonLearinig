# 获得豆瓣电影第一页数据并保存
# get请求
import urllib.request
import urllib.parse
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=0&limit=20'
headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
# （1）对象定制
request = urllib.request.Request(url=url, headers=headers)

# （2）获取对象数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# （3）下载到本地
fp = open('douban.json', 'w', encoding='utf-8')
fp.write(content)





