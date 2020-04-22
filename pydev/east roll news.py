import requests as rq
from bs4 import BeautifulSoup as bl
import shutil
import os
import time
import random
import re

meizi_headers = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36']

global headers
headers = {'User-Agent': random.choice(meizi_headers)}
urls=['https://roll.eastmoney.com/stock.html']

def roll_news(url=urls):
    global headers
    r=rq.get(url,timeout=10,headers=headers)
    html=bl(r.text,'lxml')
    news=html.find_all('a',target="_blank")
    return(news)

news_list=[]
while True:
    if len(news_list)>400:
        news_list=[]
    try:
        k=roll_news(url=urls[0])
        for i in k:
            if 'http://stock.eastmoney.com/a/' in str(i):
                if i.text in news_list:
                    pass
                else:
                    print(i.text,'  '+i.attrs['href'])
                    news_list.append(i.text)
                    with open('d:/result/stock_news.txt','a') as tar:
                        tar.write(i.text+'   '+i.attrs['href']+'  '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
    except:
        pass
    time.sleep(5)
