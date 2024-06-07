import urllib.request
import urllib.parse

# first page
# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=
# second page
# https://music.163.com/weapi/comment/resource/comments/get?csrf_token=
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {'Host': 'music.163.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
           'Accept': '*/*',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          # 'Accept-Encoding': 'gzip, deflate, br',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Content-Length': '570',
           'Origin': 'https://music.163.com',
           'Connection': 'keep-alive',
           'Referer': 'https://music.163.com/discover/toplist?id=2884035',
           'Cookie': 'NMTID=00OZbg0F05BoAYvy0X9tD79PwkPJ84AAAGK_fv4Xg; JSESSIONID-WYYY=8CjMxrnsRZ7PleD%2FlHoydO0z%2Fh9%2F9wySRoCiBje5ZK%5CKC%2BCmBpCDvawPw2Eup62vJqdKsBnsutui8TspMac1NAz7tOHj8iH2AE7UkVR%2Fo4TcJ7buZu9EQ7KQuBJN3w4S5YqdBJKRbVBv7lU0OWNKGvn7pm4gBQSbZq4DEh%2BWRBx%5CvIOe%3A1696480066188; _iuqxldmzr_=32; _ntes_nnid=cd5cbe1a53ea6dfb0775e46a30107e25,1696478266200; _ntes_nuid=cd5cbe1a53ea6dfb0775e46a30107e25; WEVNSM=1.0.0; WNMCID=bwiwca.1696478266521.01.0; csrfToken=ylA4hMZtbN7FlAOSBUoEi4JA; ntes_utid=tid._.rxuUYcspa2hARhEBEQaEnKvi%252B%252FVEZegs._.0; sDeviceId=YD-%2BfHy%2FVrr0KNFB1BVQAbEnL%2Fz6vARYLmF; WM_NI=30det0RpCeuzCMFu94nx4tSz%2Bf6FevrheVNrYbccnNGvEHXpUFHBXokkoAql9ZTrwspg85kN7yUC8ZzygCFAQy3OfTWmMwQqamA0OjwHCoMuZGybu0n8gm7rTO0J%2FkY7Z2Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4d55cadaaa295ec4494ac8ab2c84b939a8b82d172a6eaa697ae5b83be9d8caa2af0fea7c3b92af1f0ac86f73c92b08d86f87281938a96bc40aea8fc95d272e9bafaa7e87eb2b8abb7cd7a9bbead84ed4685aa8ba9db7c979a88a3db65a9b5a1a2f468fb869c93f679b4b9f8d6ea46f5a79ba4bb52baa7a9a4c54b93a7fdb0e56095b38398d47ba3b38fd1ce62b5988d90d07f9a99b783f83caee8a98eb67a989100abae619be996d3d437e2a3; WM_TID=y%2F%2B2C7MyQpFAEQEBVQKFiP6y6vRQPDwv',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           "TE": "trailers"}
data = {
	"params": "Scg0RfCMO/Iiu9nk83LM4ZCoquZc00OI5ZHOC0y1tW9vPvZVihLyAXaNuLYEnMk5HXyZZra17n2RazD40tz57zTS/HdjMx783kTX9ZgwCYoqKO1HCC5qr+O3C4NSJ2BWzNlQPUPUjgRq3GX/uYl9zcn7dt/JOiWhkivO3sWsmddGcbkDgsDUDXoEy5c2Xg83jpcc8uxO3Ll39w79Fa3txgBR0N7nUjs5vqycibqa8KZVzm8WI9iSb/yKrBeM2ZnlAHkV3Wks7U2A1PkFrxCqqA==",
	"encSecKey": "9a730e755b9583b317fbca4cc893fb70f68d2ab2c47778cf15dd149222aa12d2ca224b105da78bb9c23a36d237724f2a0d9d3f5c92ec52e88c74c80321908adec7a809b15cd708367d63d0dd99db299e5c405b601b619465a615debd701ee1b9f4d295dcd83db57882ce26cab50fe86d0a925332242e4820e4a2e67a0b3a81b7"
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open('网易云原创榜单评论区数据.json', 'w') as fp:
    fp.write(content)
