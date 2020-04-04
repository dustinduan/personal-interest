#appcode:91fa754784494761b450672aba2d3efb
#appkey:anbbjlcmg3dfu6si1uvlo61xt3xy27ti
import urllib.request as ul
import ssl
import sys
#python3示例代码下载链接
#http://code.fegine.com/python3Demo.zip

ip=input('请输入需要定位的Ip地址:')
host = 'https://ips.market.alicloudapi.com'
path = '/iplocaltion'
method = 'GET'
appcode = 'anbbjlcmg3dfu6si1uvlo61xt3xy27ti'
querys = 'ip='+ip
bodys = {}
url = host + path + '?' + querys

head={'Authorization':'APPCODE '+appcode}
request = ul.Request(url,headers=head)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response=ul.urlopen(request,context=ctx)
#content=response.read()
#if (content):
#    print(content)
print(response)