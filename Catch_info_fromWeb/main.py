import urllib.request
url = 'https://www.bilibili.com/'
res = urllib.request.urlopen(url)
src = res.read().decode('utf-8')
print(src)