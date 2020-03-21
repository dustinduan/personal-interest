#appcode:91fa754784494761b450672aba2d3efb
#appkey:anbbjlcmg3dfu6si1uvlo61xt3xy27ti
import urllib, urllib3, sys
import ssl
#python3示例代码下载链接
#http://code.fegine.com/python3Demo.zip

host = 'https://ips.market.alicloudapi.com'
path = '/iplocaltion'
method = 'GET'
appcode = 'anbbjlcmg3dfu6si1uvlo61xt3xy27ti'
querys = 'ip=127.0.0.1'
bodys = {}
url = host + path + '?' + querys

request = urllib.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)