# coding:utf-8

import urllib
import urllib2

proxy_switch = True

noproxy_handler = urllib2.ProxyHandler({})
"""
if need verify, format like this:
"http":"usr_name:passwd@58.17.125.215:53281"
"""

proxy_addr = "112.95.89.41:9999"
#proxy_addr = "171.35.103.37:808"
proxy_handler = urllib2.ProxyHandler({"http": proxy_addr})

if proxy_switch:
    myopener = urllib2.build_opener(proxy_handler)
else:
    myopener = urllib2.build_opener(noproxy_handler)

url = "http://www.whatismyip.com.tw/"
ag_head = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
}

request = urllib2.Request(url, headers=ag_head)
print(myopener.open(request).read())
