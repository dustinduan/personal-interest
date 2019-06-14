import requests as req
from bs4 import BeautifulSoup as bup
import pandas as pd
import time
def get_price_list(web_address):
    u=req.get(url=web_address.strip('\n'))
    soup=bup(u.text,'lxml')
    infor=soup.find_all('tr')
    lis=[]
    for i in infor[1:]:
        dic={}
        dic['品种名称']=i.find_all('td')[0].text.replace("\n","")
        dic['品牌与规格']=i.find_all('td')[1].text.replace("\n","")
        dic['报价']=i.find_all('td')[2].text.replace("\n","")
        dic['报价提供方']=i.find_all('td')[3].text.replace("\n","")
        dic['报价时间']=i.find_all('td')[4].text.replace("\n","")
        lis.append(dic)
    df=pd.DataFrame(lis)
    df.to_csv("price.csv",mode='a')
    
with open ('shengyishe.txt','r') as source:
    for eachline in source:
         get_price_list(eachline)
         print("succeed")
