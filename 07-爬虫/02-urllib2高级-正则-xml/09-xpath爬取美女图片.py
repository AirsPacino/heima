# coding:utf-8

import urllib
import urllib2
from lxml import etree


def load_page(url):
    """
    向网站发送请求
    :return:
    """
    ag_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

    request = urllib2.Request(url, headers=ag_header)
    html = urllib2.urlopen(request).read()

    xml_data = etree.HTML(html)
    #link_list = xml_data.xpath('//div[@class="wrappic"]//img/@src')
    link_list = xml_data.xpath('//img[@class="BDE_Image"]/@src')
    print("link_list: " + str(link_list))
    for item in link_list:
        save_image(item)


def save_image(link):
    """
    保存接收到的数据为本地图片
    :return:
    """
    ag_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    file_name = link[-16:]
    print("开始下载图片%s" % file_name)
    request = urllib2.Request(link, headers=ag_header)
    data = urllib2.urlopen(request).read()
    with open(file_name, "wb") as f:
        f.write(data)
        print("保存图片%s完成！" % file_name)


def beauty_spider():
    """
    进行总体调度
    :return:
    """
    url = "https://tieba.baidu.com/p/5498979379/"
    load_page(url)


if __name__ == '__main__':
    beauty_spider()
