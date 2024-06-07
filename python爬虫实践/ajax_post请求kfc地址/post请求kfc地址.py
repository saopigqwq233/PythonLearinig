import urllib.request
import urllib.parse
import urllib.request
import urllib.parse
def creat_request(page):  #对象定制
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {"User-Agent" :
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
    data = {
	"cname": "北京",
	"pid": "",
	"pageIndex": page,
	"pageSize": "10"}
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=url,headers=headers,data=data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_content(page,content):
    with open('KFC_LOCATION_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('输入起始页码'))
    end_page = int(input('输入结束页码'))
    for page in range(start_page,end_page+1):
        request = creat_request(page)
        content = get_content(request)
        download_content(page,content)

