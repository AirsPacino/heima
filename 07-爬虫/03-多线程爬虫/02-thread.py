# coding:utf-8

# 网站主页地址:https://9song.me/cy/%e5%ae%b6%e5%ba%ad%e4%ba%82%e5%80%ab/
# 每页的地址: page/1/
# 每篇文章的地址 //h2//@href
# 文章的标题: //h1
# 文章的内容：////div[@class="entry-inner"]

import urllib
import urllib2
import Queue
import threading
import requests
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
            # self.load_image(section_url)
            print(section_url)

    def load_image(self, section_url):
        print("[*]正在获取文章数据中...")
        request = urllib2.Request(section_url, headers=self.head)
        html = urllib2.urlopen(request).read().decode("utf-8")
        file_name = etree.HTML(html).xpath('//h1/text()')
        content_txt = etree.HTML(html).xpath('//div[@class="entry-inner"]//p/text()')
        for title in file_name:
            print("[*]正在保存文章<%s>..." % title.encode("utf-8"))
            for each_txt in content_txt:
                self.save_text(title, each_txt.encode("utf-8"))

    def save_text(self, title, each_txt):
        # print("[*]正在保存文章...")
        file_name = title + ".txt"
        with open(file_name, "ab") as f:
            f.write(each_txt + "\r\n")
        # print("[*]保存文章%s完成！！！" % file_name.encode("utf-8"))


class CrawThread(threading.Thread):
    def __init__(self, name, page_queue, each_page_queue, header):
        super(CrawThread, self).__init__(name=name)
        self.page_queue = page_queue
        self.headers = header
        self.each_page_queue = each_page_queue

    def run(self):
        print("启动%s" % self.name)
        try:
            page = self.page_queue.get(False)
            full_url = "https://9song.me/cy/%e6%a0%a1%e5%9c%92%e5%ad%b8%e7%94%9f/page/" + str(page)
            html = requests.get(full_url, self.headers).text
            self.each_page_queue.put(html)
        except:
            pass
        print("结束%s" % self.name)


class ParseThread(threading.Thread):
    def __init__(self, thread_name, data_queue, mylock):
        super(ParseThread, self).__init__(name=thread_name)
        self.lock = mylock
        self.data_queue = data_queue

    def run(self):
        print("启动%s" % self.name)
        """这里的html是每一篇文章的页面的html源码"""
        html = self.data_queue.get()
        self.handle(html)

    def handle(self, html):
        file_name = etree.HTML(html).xpath('//h1/text()')
        content_txt = etree.HTML(html).xpath('//div[@class="entry-inner"]//p/text()')
        for title in file_name:
            print("[*]正在保存文章<%s>..." % title.encode("utf-8"))
            for each_txt in content_txt:
                self.save_text(title, each_txt.encode("utf-8"))

    def save_text(self, title, each_txt):
        file_name = title + ".txt"
        with open(file_name, "ab") as f:
            f.write(each_txt + "\r\n")
        print("[*]保存文章%s完成！！！" % file_name.encode("utf-8"))


class CrawEachThread(threading.Thread):
    def __init__(self, thread_name, each_page_queue, data_queue, header):
        super(CrawEachThread, self).__init__(thread_name)
        self.each_page_queue = each_page_queue
        self.data_queue = data_queue
        self.header = header

    def run(self):
        print("启动%s" % self.name)
        try:
            html = self.each_page_queue.get(False)
            self.handle(html)
        except:
            pass
        print("结束%s" % self.name)

    def handle(self, html):
        path_list = etree.HTML(html).xpath('//h2//a/@href')
        for section_url in path_list:
            each_html = requests.get(section_url)
            self.data_queue.put(each_html)


if __name__ == '__main__':

    """基本信息"""
    url = "https://9song.me/cy/%e6%a0%a1%e5%9c%92%e5%ad%b8%e7%94%9f/page/"
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

    mylock = threading.Lock()

    """所需队列"""
    page_queue = Queue.Queue()
    data_queue = Queue.Queue()
    each_page_queue = Queue.Queue()

    """用户输入请求的指定页面"""
    start_page = int(raw_input("起始页："))
    end_page = int(raw_input("结束页："))

    """先put需要爬取的页数"""
    for page in range(start_page, end_page + 1):
        page_queue.put(page)

    """启动采集线程..."""
    craw_list = ["craw-1", "craw-2", "craw-3"]
    craw_thread = []

    for thread_name in craw_list:
        thread = CrawThread(thread_name, page_queue, each_page_queue, ag_header)
        thread.start()
        craw_thread.append(thread)

    """获取每一页的url"""
    craw_each_page = ["each-1", "each-2", "each-3"]
    craw_each_thread = []

    for thread_name in craw_each_page:
        thread = CrawEachThread(thread_name, each_page_queue, data_queue, ag_header)
        thread.start()
        craw_each_thread.append(thread)

    """启动解析线程..."""
    parse_list = ["parse-1", "parse-2", "parse-3"]
    parse_thread = []

    """需要的初始化参数不同"""
    for parse_name in parse_list:
        thread = ParseThread(parse_name, data_queue, mylock)
        thread.start()
        parse_thread.append(thread)

        # print("[*]正在爬取此分类下第%d页..." % page)
        # sexy = Spider(full_url, ag_header)
        # sexy.load_page()
