import requests
import re
# from requests import requests
# response= get('http://www.baidu.com')
# print(response.status_code)  #打印状态码
# print(response.url)  #打印请求url
# print(response.headers)  #打印头部
# print()
# print(response.cookies)  #打印cookie
# print(response.text)   #以文本形式打印网页源码
# print(response.content)  #以字节流形式打印网页源码
# print('=================================================================')
# data={'word':'hello'} #表单参数
# #对需要爬取的网页发送请求
# response=requests.post('http://httpbin.org/post',data=data)
# print(response.content)

url='https://www.xiazaitxt.net/top/allvisit/1.html'
resp=requests.get(url)
resp.encoding='gbk'                 #指定字符集
s=resp.text

obj=re.compile(r'<div class="panel-body">.*?<div class="col-md-4 col-xs-4 book-coverlist">.*?alt="(?P<NAME>.*?)"></a>.*?<small class="text-muted fs-12">(?P<user>.*?)</small>.*?</div>',re.S)
result=obj.finditer(s)
for i in result:
    a = i.group('NAME')
    b = i.group('user')
print(a,b)

