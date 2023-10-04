import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
'Host':'fanyi.baidu.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
'Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding':'gzip, deflate, br',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Acs-Token':'1696419199015_1696419209545_oWnfLNMmnscz1+I3WX0sXr52KF6UxVvrwqsiN5FLyytorOHhnimk1sYy1hthdsYyXYuFM3acWkCIqq7TZw80otzRenRt4kvRy36VQKkrUtOm2JhrUt0zl7sne285ivGuHRgJl7SMpzyRVu9oeFKnKQsIoDyfPhh81TL3kCJqSH3RSqHVcGrw25FoftgRZVt8IFOjM6LYW6m8mJfK+gaRICtSp18ETb7le9PPwk7mSpodW5QFU5E/zjhwSgKlQUoQW1rh+o8ePuCp0B4qVPlr/GzuqzTY/wEyiNP/ivii0rWAq5zWx+SbkkL4Cc2T0/9hp3+0iP+1SMTr2fAusnfLsgcDpnNHsXoBVfa9ZBFVbSFJK6E4cteBAEqJV3oFiglfFLDtE/G/Kf+pB+B33U5/sO3Qpt4WdZhYnrTWCr2vg5EUXoyYg1vkkCYyc/2S6yZEiiznumTMd3GJsl251n+uIQ==',
'X-Requested-With':'XMLHttpRequest',
'Content-Length':'148',
'Origin':'https://fanyi.baidu.com',
'Connection':'keep-alive',
'Referer':'https://fanyi.baidu.com/',
'Cookie':'BAIDUID=EDBE60A449F97F326F322502BC50B579:FG=1; BIDUPSID=EDBE60A449F97F321A4506359EB4826E; PSTM=1696329859; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=012005810h8hal0h2h2k2g211ihoc6a1o; ZFY=QOsyPnMyhhFe9SnQXILmHgw7f0cJvHQmBqloCtkpNm4:C; RT="z=1&dm=baidu.com&si=8a695e99-3cbf-469d-8b9c-8352cf1676dc&ss=lnb9gqfr&sl=w&tt=j5w&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=6jhb&ul=c4t1&hd=c4ws"; __bid_n=18af60aa7888432b2cb274; PSINO=1; H_PS_PSSID=39313_39354_39396_39407_39097_39358_39375_39461_39233_39403_26350_39428; delPer=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1696411932; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1696419199; APPGUIDE_10_6_5=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZGU5ZjZkY2M3NzBmYzExZjcyZGZjNTgwMWU3NTg3NDViMWIzMzU1Y2QxMjY3MzhlZGNjOGIzZTI2Nzk4N2MyYzYzYzcyY2NhYjc3OWQ1OTM1Y2M2N2VmZDNiNWM0OTBkNzcwNDI0MGIzNDc4N2QxMzU0Y2ZhMWVjMmU5OTBhNGJlYWMxY2JmNjA0Y2IwODQwMzZlYTQwMWExOWU4Njk4Mg==',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
}
data = {
    "from": "en",
    "to": "zh",
    "query": "good",
    "transtype": "enter",
    "simple_means_flag": "3",
    "sign": "262931.57378",
    "token": "67f4d4655cc8b1f9fecadf26cdb90c2d",
    "domain": "common",
    "ts": "1696419209526"
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(json.loads(content))
