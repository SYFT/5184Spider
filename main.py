# -*- coding: utf-8 -*-

# package import
import urllib, urllib2, cookielib
from config import *

# build opener
cookie = cookielib.MozillaCookieJar(cookie_file)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

print "Spider begin:"

# main procedure
post_data = None
request = urllib2.Request(query_web_url, post_data, default_headers)
response = opener.open(request, timeout=1000)
print "Successfully open query web."

while True :
    #urllib.urlretrieve(checkcode_url, checkcode_file)
    request = urllib2.Request(checkcode_url, post_data, getCheckcode_headers)
    response = opener.open(request, timeout=1000)
    file = open(checkcode_file, "wb")
    file.write(response.read())
    file.close()
    print "Successfully download checkcode."
    
    user_checkcode = raw_input("Please input checkcode according to local checkcode picture.")
    first_data = {
                  "csny":"9801",
                  "zkzh":"2000102442",
                  "yzm":user_checkcode
                  }
    post_data = urllib.urlencode(first_data)
    request = urllib2.Request(query_url, post_data, query_headers)
    response = opener.open(request, timeout=1000)
    result = response.read()
    print result
    print result.find(u"\u9519\u8bef")
    if result.find(u"\u9519\u8bef") == -1 :
        break


first_data = {
              "csny":"9801",
              "zkzh":"2000102442",
              "yzm":"1111"
              }
post_data = urllib.urlencode(first_data)
request = urllib2.Request(query_url, post_data, query_headers)
response = opener.open(request, timeout=1000)
result = unicode(response.read())
print result.decode("unicode_escape")

cookie.save(ignore_discard=True, ignore_expires=True)

# main prpcedure
