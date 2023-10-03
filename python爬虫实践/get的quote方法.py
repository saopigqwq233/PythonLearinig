import urllib.request
import urllib.parse
# https://www.bing.com/search?form=MOZTSB&pc=MOZI&q=%E5%91%A8%E6%9D%B0%E4%BC%A6
name = urllib.parse.quote('毛不易')
url = 'https://www.bing.com/search?form=MOZTSB&pc=MOZI&q='+name
header = {"User-Agent" :
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
ask_forWeb = urllib.request.Request(url=url,headers=header)

res = urllib.request.urlopen(ask_forWeb)

src = res.read().decode('utf-8')

print('毛不易' in str(src))


