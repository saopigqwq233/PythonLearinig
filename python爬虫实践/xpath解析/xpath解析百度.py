# coding=gb2312
import urllib.request
import urllib.parse
from lxml import etree
url = 'https://blog.csdn.net/nanxun_198/category_11467091.html'
headers = {"User-Agent" :
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

# ������������ӦԴ��
tree = etree.HTML(content)

#��ȡ��Ҫ������

result = tree.xpath('//h3[@title="Pythonѧϰ�ʼ�"]/text()')[0]

print(result)

