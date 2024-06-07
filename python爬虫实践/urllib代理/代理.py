import urllib.request
import urllib.parse
url = 'https://ip.skk.moe/'
headers = {
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# # 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
# 'Cache-Control':'max-age=0',
# 'Connection':'keep-alive',
# 'Cookie':'__bid_n=18978e3cb729296ca16143; BAIDU_WISE_UID=wapp_1690358469481_30; BAIDUID=D67A38C8C29FEBF704A90E38ACE7D018:FG=1; BAIDUID_BFESS=D67A38C8C29FEBF704A90E38ACE7D018:FG=1; jsdk-uuid=7a725eca-7241-4661-907b-8fd842eaa921; BIDUPSID=D67A38C8C29FEBF704A90E38ACE7D018; PSTM=1690940215; ZFY=u77Ed0afUWMcMjA9hcuPwINN1WlVly1VwTfafiQHhiA:C; BDUSS=kwbDJOa2pIb2JpMmtIbkxrdnUwdG1oV0x5ZHVRQ2RnQX5ORkdGNTBZY1R1a1ZsRVFBQUFBJCQAAAAAAQAAAAEAAACQGp42AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABMtHmUTLR5lSl; BDUSS_BFESS=kwbDJOa2pIb2JpMmtIbkxrdnUwdG1oV0x5ZHVRQ2RnQX5ORkdGNTBZY1R1a1ZsRVFBQUFBJCQAAAAAAQAAAAEAAACQGp42AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABMtHmUTLR5lSl; BD_UPN=12314753; BA_HECTOR=0k8520aha1a10h0k8h8l80a11iii74p1o; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; delPer=0; H_PS_PSSID=39316_39360_39396_39419_39412_39437_39480_39479_39461_39234_39405_39486_26350_39429; COOKIE_SESSION=4_0_0_3_0_1_1_0_0_1_0_0_0_0_0_0_0_0_1693453348%7C3%230_0_1693453348%7C1; ab_sr=1.0.1_M2UxOWFiOWZiZDk1OTdiZDUzZjZlYThmODlkNTVjY2JkYzQ5MGJmMDMxYmUwNzI2MjM0YzBiNDM2MmM2M2JkM2EyOTI0M2ZjYWE0YjBjMGQ5YWIwOWI4OTUzYmZkMTFkOGExZTVmZDIyNTE3NTIwN2E0ZDE2ODdjMmViZmIyOTZjN2RkMTdhNGQ3ZjQ5MjA1NjA4OGRjNjE1NmFiZDBhMA==; PSINO=2; H_PS_645EC=e046h97lA0%2BbWGsgcYWBHxruFWJ9kFqYhMn8SfsGwF51qsBx6Tg37tgsYFw; baikeVisitId=3e43ed65-b894-4aa4-9df5-d0370fa74e71',
# 'Host':'www.baidu.com',
# 'Sec-Ch-Ua':'"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
# 'Sec-Ch-Ua-Mobile':'?0',
# 'Sec-Ch-Ua-Platform':'"Windows"',
# 'Sec-Fetch-Dest':'document',
# 'Sec-Fetch-Mode':'navigate',
# 'Sec-Fetch-Site':'none',
# 'Sec-Fetch-User':'?1',
# 'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
}
request = urllib.request.Request(url=url,headers=headers)


proxies = {
    'http':'113.121.21.103:9999'
}
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)




