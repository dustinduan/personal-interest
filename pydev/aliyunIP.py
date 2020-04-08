import sys
import json
import urllib.request as ul


def ip_search(ip):
    host = 'http://saip.market.alicloudapi.com'
    path = '/ip'
    method = 'GET'
    appcode = '91fa754784494761b450672aba2d3efb'
    querys = 'ip='+ip
    bodys = {}
    url = host + path + '?' + querys
    head={'Authorization':'APPCODE '+appcode}
    request = ul.Request(url,headers=head)
    response = ul.urlopen(request)
    content = response.read()
    info=json.loads(content)
    return(info)
ip=input('请输入需要查询的IP地址:')
info=ip_search(ip)
k=info['showapi_res_body']
print('IP地址对应的信息如下:'+'\n')
for i in k:
    print(i,k[i])
c=input('请按任意键结束查询。。。。。。')
