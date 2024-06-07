
# 下载多页数据
# 第一页  https://sc.chinaz.com/tupian/chengshijingguantupian.html
# 第二页  https://sc.chinaz.com/tupian/chengshijingguantupian_2.html

import urllib.request
import urllib.parse
from lxml import etree


def creat_request(page):
    headers = {
        'Host': 'sc.chinaz.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://sc.chinaz.com/tupian/',
        'Connection': 'keep-alive',
        'Cookie': 'cz_statistics_visitor=c4bcaa6c-a01d-c841-eac9-df068c15e682; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1697260413; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1697271263',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/chengshijingguantupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/chengshijingguantupian_' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_img(content):
    # 获取网络源码，下载图片
    # urllib.request.urlretrieve('图片地址','文件名称')
    # xpath解析源码，获取图片地址
    tree = etree.HTML(content)
    # /html/body/div[3]/div[2]/div[1]/img
    # /html/body/div[3]/div[2]/div[2]/img
    # /html/body/div[3]/div[2]/div[3]/img
    name_list = tree.xpath('/html/body/div[3]/div[2]//img/@alt')
    url_list = tree.xpath('/html/body/div[3]/div[2]//img/@data-original')
    dic = dict(zip(name_list,url_list))
    for name,url in dic.items():
        url = 'https:'+url
        name = name + '.jpg'
        urllib.request.urlretrieve(url=url,filename='./cityImg/'+name)



if __name__ == '__main__':
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        download_img(content)





