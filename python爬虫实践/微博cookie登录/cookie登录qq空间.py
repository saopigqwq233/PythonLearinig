import urllib.request
import urllib.parse

url = 'https://user.qzone.qq.com/904139266'
headers = {'Host': 'user.qzone.qq.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           # 'Accept-Encoding':'gzip, deflate, br',
           'Referer': 'https://qzs.qq.com/',
           'Connection': 'keep-alive',
           'Cookie': 'RK=FO3RolDYGN; ptcz=d15feb55c05977b30d82aa410ad3f08c76c064ce034ac4e031113334765839b8; pac_uid=0_ppFhSmtAHBkj1; _qpsvr_localtk=0.32336128604325776; pgv_pvid=4711807693; pgv_info=ssid=s8593071388; uin=o0904139266; skey=@bDGBieE0s; p_uin=o0904139266; pt4_token=935xt7o-zaRm8dETruX6FW1KqZvJ-U8xhNJVRVYXTyU_; p_skey=oSeOKQl9hQjOHpJwNn3Sx*VW7NeblZhKOp7s2omBPm4_; Loading=Yes; x-stgw-ssl-info=3ab48dee5b95fae2f518f3a4521d1a5e|0.137|-|1|.|Y|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|32785|h2|0; qz_screen=1536x864; 904139266_todaycount=0; 904139266_totalcount=5904; QZ_FE_WEBP_SUPPORT=1',
           'Upgrade-Insecure-Requests': '1',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-site',
           'Sec-Fetch-User': '?1',
           'Pragma': 'no-cache',
           'Cache-Control': 'no-cache',
           'TE': 'trailers'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('qq.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
