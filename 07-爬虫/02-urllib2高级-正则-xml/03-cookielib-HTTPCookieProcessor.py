import urllib
import urllib2
import cookielib

"""
cookieJar: ==>save cookie
    FileCookieJar 
        MozillaCookieJar    LWPCookieJar(set-cookie3)
"""

cookie = cookielib.CookieJar()

cookie_handler = urllib2.HTTPHandler()

openner = urllib2.build_opener(cookie_handler)

url = ""
ag_head = {}
raw_data = {"email":"test@test.com", "passwd":"password"}
data = urllib.urlencode(raw_data)

request = urllib2.Request(url, data=data, headers=ag_head)
print(openner.open(request).read())

# then you can many times ==> openner.open()