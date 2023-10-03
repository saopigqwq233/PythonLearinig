import urllib.request
url = 'https://www.baidu.com/'
res = urllib.request.urlopen(url)
# 读完
"""src = res.read()
print(src)
"""
# 读几个字节
"""src = res.read(5)
print(src)
"""
# 读行
"""src = res.readline()
print(src)
"""
# 读几行,把每行作为列表元素
"""src = res.readlines()
print(src)
"""
# 状态码 200ok 404error
# print(res.getcode())
# 返回url
"""print(res.geturl())
"""
# 获取状态信息
print(res.getheaders())



