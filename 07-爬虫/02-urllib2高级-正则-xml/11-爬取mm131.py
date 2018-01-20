# coding:utf-8

import urllib
import urllib2
from lxml import etree


class Spider(object):

    def __init__(self, url, ag_header):
        self.url = url
        self.head = ag_header

    def load_page(self):
        print("[*]获取页面中每个版块的url中...")
        request = urllib2.Request(self.url, headers=self.head)
        html = urllib2.urlopen(request).read().decode("gbk")
        print(html)
        path_list = etree.HTML(html).xpath('//li[@class="column-li"]//a/@href')
        for section_url in path_list:
            self.load_image(section_url)

    def load_image(self, section_url):
        print("[*]正在获取图片url地址中...")
        request = urllib2.Request(section_url, headers=self.head)
        html = urllib2.urlopen(request).read().decode("gbk")
        img_url_list = etree.HTML(html).xpath('//div[@class="content-pic"]//img/@src')
        print(img_url_list)
        for img_url in img_url_list:
            self.save_img(img_url)

    def save_img(self, img_url):
        print("[*]正在保存图片...")
        request = urllib2.Request(img_url, headers=self.head)
        image_data = urllib2.urlopen(request).read()
        file_name = img_url[-10:-6] + ".jpg"
        with open(file_name, "wb") as f:
            f.write(image_data)
        print("[*]保存图片%s完成！！！" %file_name)


if __name__ == '__main__':
    url = "http://www.mm131.com"
    ag_header = {
        "Host" : " www.mm131.com",
        "Connection" : " keep-alive",
        "Cache-Control" : " max-age=0",
        "Upgrade-Insecure-Requests" : " 1",
        "User-Agent" : " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept" : " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer" : "http://www.mm131.com/xinggan/2229.html",
        "Accept-Language" : " zh-CN,zh;q=0.9"
    }

    sexy = Spider(url, ag_header)
    sexy.load_page()
