# coding:utf-8
"""这个程序目前还有问题。。拿不到指定数据"""
import urllib
import urllib2

word = raw_input("请输入要翻译的内容：")

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

ag_header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}

form_data = {
    "i":word,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    #"client":"fanyideskweb",
    #"salt":"1515900705926",
    #"sign":"3b75284af51b84141aced9fc1e9be015",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION",
    "typoResult":"false"
}

print(form_data)
print("*" * 30)

data = urllib.urlencode(form_data)
print(data)
print("*" * 30)

request = urllib2.Request(url, data, ag_header)

print urllib2.urlopen(request).read()
print("*" * 30)
