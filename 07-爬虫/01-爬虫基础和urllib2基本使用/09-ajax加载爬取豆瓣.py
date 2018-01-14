# coding:utf-8

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

ag_head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}

formdata = {
    "start":"0",
    "limit":"20"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=ag_head)

print(urllib2.urlopen(request).read())