import urllib.request
import urllib.parse


# 第一页
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&
# start=0&limit=20
# 第二页
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&
# start=20&limit=20
# 第三页
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&
# start=40&limit=20
# 第四页
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&
# start=60&limit=20
# 第五页
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&
# start=80&limit=20

# 第n页
# 。。。
# &start=(n-1)*20&limit=20

def creat_request(_page):
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&'
    data = {
        'start': (_page - 1) * 20,
        'limit': 20
    }
    url = base_url + urllib.parse.urlencode(data)
    _request = urllib.request.Request(url=url, headers=headers)
    return _request


def get_content(_request):
    response = urllib.request.urlopen(_request)
    _content = response.read().decode('utf-8')
    return _content


def download_content(_page, _content):
    with open('douban_' + str(_page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(_content)


# 程序入口
if __name__ == '__main__':
    start_page = int(input('输入起始页码'))
    end_page = int(input('输入结束页面'))

    for page in range(start_page, end_page + 1):
        # 每一页都定制
        request = creat_request(page)
        # 针对每一页定制的请求进行接受响应
        content = get_content(request)
        # 针对每次响应下载对应页面的json
        download_content(_page=page, _content=content)
