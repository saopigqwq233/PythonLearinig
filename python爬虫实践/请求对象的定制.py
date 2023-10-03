import urllib.request

url = 'https://www.baidu.com'
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
# url组成
# http/https www.baidu.com
# 协议     主机      端口号
# http    80
sub_forWeb = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(sub_forWeb)
src = res.read().decode('utf8')
print(src)






