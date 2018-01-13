# coding:utf-8
# 在python3中变为了urllib.request
# import urllib.request

"""
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8

"""
import urllib2

ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
url = "http://www.baidu.com/"

request = urllib2.Request(url, headers=ua_headers)

http_obj = urllib2.urlopen(request)
html = http_obj.read()

print http_obj.getcode()
#print(html)

