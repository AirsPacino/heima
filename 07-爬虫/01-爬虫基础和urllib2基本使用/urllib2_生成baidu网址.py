# coding:utf-8

import urllib
import urllib2

url = "http://www.baidu.com/"
query_str = raw_input("请输入要查询的关键字: ")

ag_headers = {"User-agent": "Mozilla sue"}
key_word = {"wd": query_str}
encode_kw = urllib.urlencode(key_word)
fullurl = url + "s?" + encode_kw
print(fullurl)

# request = urllib2.Request(fullurl, headers=ag_headers)
# obj = urllib2.urlopen(request)
# html = obj.read()
# print(html)
