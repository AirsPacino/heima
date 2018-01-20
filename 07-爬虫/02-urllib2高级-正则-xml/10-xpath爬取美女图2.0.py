# coding:utf-8

import urllib
import urllib2
from lxml import etree

"""
首先要得到这个贴吧某一页的html页面 ==> load_page()，xpath解析+拼接得到此页每个帖子的url地址
然后得到各个帖子的html页面 ==> load_image()
xpath解析得到图片的链接地址link ==> save_image(link)
sexy_spider()总体调度
"""


def load_page(url):
    """
    得到每个帖子的url地址
    :return:
    """
    print(url)
    print("正在获取此页帖子url信息" + '=' * 30)
    #ag_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    request = urllib2.Request(url)
    e_html = urllib2.urlopen(request).read()
    xml_content = etree.HTML(e_html)

    relative_path = xml_content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    print(relative_path)
    for i in relative_path:
        tiezi_url = "http://tieba.baidu.com" + i
        load_image(tiezi_url)


def load_image(tiezi_url):
    """
    得到图片的url地址
    :return:
    """
    print("正在分析图片url信息" + '=' * 30)
    ag_head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    request = urllib2.Request(tiezi_url, headers=ag_head)
    i_html = urllib2.urlopen(request).read()
    content = etree.HTML(i_html)
    link_list = content.xpath('//div[@class="p_content  "]/cc/div/img/@src')
    for link in link_list:
        save_img(link)


def save_img(link):
    """
    请求图片数据并保存到本地
    :param link:
    :return:
    """
    print("正在请求图片数据" + '=' * 30)
    ag_head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    request = urllib2.Request(link, headers=ag_head)
    image_data = urllib2.urlopen(request).read()
    file_name = link[-15:]
    print("开始保存图片%s" %file_name)
    with open(file_name, "wb") as f:
        f.write(image_data)
    print("图片%s保存完成" %file_name)


def sexy_spider(tieba, start_page, end_page):
    """
    总体调度
    :return:
    """
    """https://tieba.baidu.com/f?kw=美女&pn=0"""

    root_url = "http://tieba.baidu.com/f?"
    kw = urllib.urlencode({"kw" : tieba})

    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        url = root_url + kw + "&pn=" + str(pn)
        load_page(url)


if __name__ == '__main__':

    tieba = raw_input("请输入贴吧名：")
    start_page = int(raw_input("请输入起始页: "))
    end_page = int(raw_input("请输入结束页: "))

    sexy_spider(tieba, start_page, end_page)