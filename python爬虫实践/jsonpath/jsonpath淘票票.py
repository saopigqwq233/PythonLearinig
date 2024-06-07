# coding=gb2312
import json
fp = open('store.json','r')
obj = json.load(fp,encodings='utf8')
print(obj)
# 书店所有书的作者
