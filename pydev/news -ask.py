import os
import time

def news_read(keyword=None):
    news_list=[]
    if keyword==None:
        with open('d:/result/stock_news.txt','r') as sou:
            for eachline in sou:
                if today in eachline:
                    news_list.append(eachline.strip('\n'))
    else:
        with open('d:/result/stock_news.txt','r') as sou:
            for eachline in sou:
                if today in eachline and keyword in eachline:
                    news_list.append(eachline.strip('\n'))
        time.sleep(60)
    for i in news_list[-30:-1]:
        print(i)
    c=input()

today=time.strftime("%Y-%m-%d",time.localtime())
key=input('请输入需要查询的股票名称:')
while True:
    news_read(keyword=key)
    os.system('cls')
