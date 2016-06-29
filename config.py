# -*- coding: utf-8 -*-

# url configuration
base_url = "http://www.5184.com/gk/"
query_web_url = base_url + "check_index.html"
checkcode_url = base_url + "common/checkcode.php"
query_url = base_url + "/common/get_mem.php"

# cookie file configuration
import os
base_file = os.path.abspath('.')
cookie_file = os.path.join(base_file, "cookie.txt")
checkcode_file = os.path.join(base_file, "checkcode.jpg")

# spider configuration
default_headers = {
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Accept-Encoding":"gzip, deflate, sdch",
                   "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                   "Cache-Control":"max-age=0",
                   "Connection":"keep-alive",
                   "Host":"www.5184.com",
                   "If-Modified-Since":"Sat, 25 Jun 2016 14:03:56 GMT",
                   "If-None-Match":'"576e8f4c-acd8"',
                   "Upgrade-Insecure-Requests":"1",
                   "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
                   }
getCheckcode_headers = {
                        "Accept":"image/webp,image/*,*/*;q=0.8",
                        "Accept-Encoding":"gzip, deflate, sdch",
                        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                        "Cache-Control":"max-age=0",
                        "Connection":"keep-alive",
                        "Host":"www.5184.com",
                        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                        "Referer":"http://www.5184.com/gk/check_index.html"
                        }
query_headers = {
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                "Content-Type":"application/x-www-form-urlencoded",
                "Connection":"keep-alive",
                "Host":"www.5184.com",
                "Content-Length":"34",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                "X-Requested-With":"XMLHttpRequest",
                "Origin":"http://www.5184.com",
                "Referer":"http://www.5184.com/gk/check_index.html"
               }

DX = [-1, -1, -1, 0, 0, 1, 1, 1]
DY = [-1, 0, 1, -1, 1, -1, 0, 1]
TIMES_DENOISE = 5