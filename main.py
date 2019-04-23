import urllib2
import urllib
import cookielib
import time
#url = 'https://iaaa.pku.edu.cn/iaaa/oauthlogin.do'
#url = 'http://elective.pku.edu.cn/elective2008/edu/pku/stu/elective/controller/electiveWork/showResults.do'
url = 'http://elective.pku.edu.cn/elective2008/edu/pku/stu/elective/controller/supplement/SupplyCancel.do'
'''
postdata = {
    'appid': 'syllabus',
    'userName': '1600012867',
	'password': 'xiao201278',
	'randCode': '',
	'smsCode': '',
	'otpCode': '',
	'redirUrl': 'http://elective.pku.edu.cn:80/elective2008/ssoLogin.do'
}
'''
#cookie = cookielib.CookieJar()
#cookie = cookielib.MozillaCookieJar("fuck.txt")
newer = False
cookie = cookielib.MozillaCookieJar("fuck.txt")
if not newer:
    cookie.load("fuck.txt", ignore_expires=True, ignore_discard=True)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)#cookie is handled like this
if newer:
    opener.addheaders.append(('Cookie',
                    'JSESSIONID=F0p1c10GFkThQlJcWhvCgXvGB0k0P418nGGhbpMG21j4vcYtm7DL!102195821'))
postdata = {}
data = urllib.urlencode(postdata)
headers = {
    "Host": "elective.pku.edu.cn",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Referer": "http://elective.pku.edu.cn/elective2008/edu/pku/stu/elective/controller/electiveWork/ElectiveWorkController.jpf",
    "Upgrade-Insecure-Requests": 1
}
request = urllib2.Request(url = url, headers = headers)
response = opener.open(request)
html = response.read()
print html
print "-------hips---------"
print int(round(time.time() * 1000))
print "--------now---------"
for item in cookie:
    print item
cookie.save(ignore_discard=True, ignore_expires=True)
