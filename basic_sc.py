import builtwith as bt
import whois
import urllib.request as ul
import urllib3 as ul_3
import re
import itertools
import time
#urllib是一个包含几个模块来处理请求的库。分别是：
#    request.urlopen(url, data=None, timeout=10)
#    import ssl
#    解决某些环境下报<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
#    ssl._create_default_https_context = ssl._create_unverified_context
#    url = 'https://www.jianshu.com'
#    返回<http.client.HTTPResponse object at 0x0000000002E34550>
#    response = request.urlopen(url, data=None, timeout=10)
#    直接用urllib.request模块的urlopen()获取页面，page的数据格式为bytes类型，需要decode()解码，转换成str类型。
#    page = response.read().decode('utf-8')
#urllib.request 发送http请求
#urllib.error 处理请求过程中,出现的异常。
#urllib.parse 解析url
#urllib.robotparser 解析robots.txt 文件
website='https://www.xiashutxt.com/209558/'
#ch=bt.parse(website)
#ower=whois.whois(website)
prog_re=re.compile(r"(?<=<br/>).*?(?<=<br/>)")
#print(ch)
#print(ower)

def download(url,num_retries=3):
    print("Download",url)
    try:
        html=ul.urlopen(url).read()
    except ul.URLError as e:
        print("网页下载失败",e.reason)
        if num_retries>0:
            if hasattr(e,'code') and 500<e.code<600:
                return (download(url,num_retries-1))
        html=None
    return (html)

def pc_download(url,num_retries=3):#模拟windows电脑来搜集目标网页下面的网络链接
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    request=ul.Request(url,headers=headers)
    response=ul.urlopen(request)
    with response as f:
        print('Status:',f.status,f.reason)
        for k,v in f.getheaders():
            print("%s"%v)
        print('Data:',f.read().decode('utf-8'))
    #print(request.get_method())
    #print(response.read())
    return(response.read())

def iphone_download(url,num_retries=3):#模拟Iphone手机来收集目标网页下面的存在的链接
    req=ul.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) ''AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with ul.urlopen(req) as f:
        print('Status:',f.status,f.reason)
        for k,v in f.getheaders():
            print("%s %s"%(k,v))
        print('Data:',f.read().decode('utf-8'))

def page_get():
    max_errors=5
    num_errors=0
    for page in itertools.count(1):#利用数字ID来进行遍历
        url='https://www.xiashutxt.com/209558/read_%d.html'%page
        html=prog_re.match(download(url).decode('utf-8'))
        if html is None:
            num_errors+=1
            if num_errors==max_errors:
                break
        else:
            num_errors=0
            with open('newnovel.txt','ab') as tar:
                tar.write(html)
            pass
            time.sleep(1)

def get_links(url):
    webpage_list=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    value=webpage_list.findall(url.decode('utf-8'))
    for i in value:
        print (i)

get_links(download(website))
