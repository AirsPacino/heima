# coding:utf-8
"""爬取指定贴吧的指定页数，并将html页面保存到本地"""

import urllib
import urllib2

def load_page(full_url):
    """
    向服务器发送请求,获取到html页面的数据
    :return:
    """
    ag_header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    request = urllib2.Request(full_url, headers=ag_header)
    html_obj = urllib2.urlopen(request)
    return html_obj.read()

def write_page(html, file_name):
    """
    将接收到的html保存为html文件
    :param html:接收道德html数据
    :return:
    """
    print("正在保存页面%s" %file_name)
    with open(file_name, "w") as f:
        f.write(html)

def tiebaSpider(tieba_name, start_page, end_page):
    """
    进行总体调度，每个函数执行的顺序等等
    :return:
    """
    url = "http://tieba.baidu.com/f?"
    kw = urllib.urlencode({"kw": tieba_name})
    for page in range(start_page, end_page + 1):
        pn = (page-1) * 50
        full_url = url + kw + "&pn=" + str(pn)
        file_name = tieba_name + "page" + str(page) + ".html"
        print(full_url)
        print("正在下载页面%s" %file_name)
        html = load_page(full_url)
        write_page(html, file_name)


if __name__ == '__main__':
    tieba_name = raw_input("请输入贴吧名: ")
    start_page = int(raw_input("起始页: "))
    end_page = int(raw_input("终止页: "))

    tiebaSpider(tieba_name, start_page, end_page)

