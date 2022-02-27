import urllib.request
response=urllib.request.urlopen('http://www.baidu.com')
html=response.read()  #读取网页代码
print(html ,'\t')
print(type(html))

