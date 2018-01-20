# coding:utf-8

# 网站主页地址:https://9song.me/cy/%e5%ae%b6%e5%ba%ad%e4%ba%82%e5%80%ab/
# 每页的地址: page/1/
# 每篇文章的地址 //h2//@href
# 文章的标题: //h1
# 文章的内容：////div[@class="entry-inner"]

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
        html = urllib2.urlopen(request).read().decode("utf-8")
        path_list = etree.HTML(html).xpath('//h2//a/@href')
        for section_url in path_list:
            #self.load_image(section_url)
            print(section_url)

    def load_image(self, section_url):
        print("[*]正在获取文章数据中...")
        request = urllib2.Request(section_url, headers=self.head)
        html = urllib2.urlopen(request).read().decode("utf-8")
        file_name = etree.HTML(html).xpath('//h1/text()')
        content_txt = etree.HTML(html).xpath('//div[@class="entry-inner"]//p/text()')
        for title in file_name:
            print("[*]正在保存文章<%s>..." %title.encode("utf-8"))
            for each_txt in content_txt:
                self.save_text(title, each_txt.encode("utf-8"))

    def save_text(self, title, each_txt):
        #print("[*]正在保存文章...")
        file_name = title + ".txt"
        with open(file_name, "ab") as f:
            f.write(each_txt + "\r\n")
        #print("[*]保存文章%s完成！！！" % file_name.encode("utf-8"))



if __name__ == '__main__':
    url = "https://9song.me/cy/%e5%ae%b6%e5%ba%ad%e4%ba%82%e5%80%ab/"
    ag_header = {
        "Host": " 9song.me",
        "Connection": " keep-alive",
        # "Cache-Control" : " max-age=0",
        "Upgrade-Insecure-Requests": " 1",
        # "User-Agent" : " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        # "User-Agent" : "Mozilla/5.0(compatible;MSIE 9.0; Windows NT6.1;Trident/5.0)",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": " zh-CN,zh;q=0.9"
    }

    start_page = int(raw_input("起始页："))
    end_page = int(raw_input("结束页："))
    for page in range(start_page, end_page + 1):
        full_url = url + "page/" + str(page)
        print("[*]正在爬取此分类下第%d页..." % page)
        sexy = Spider(full_url, ag_header)
        sexy.load_page()
