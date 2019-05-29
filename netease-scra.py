import requests as req
from bs4 import BeautifulSoup as bup
import pandas as pd
basic_web='https://book.douban.com/latest'
u=req.get(url=basic_web)
#print(u)验证是否访问成功
soup=bup(u.text,'lxml')
infor=soup.find_all('div',class_="detail-frame")
lis=[]
for i in infor:
    dic={}
    dic['书名']=i.h2.text.replace("\n","")
    dic['评分']=i.find_all('p')[0].text.replace("\n","").replace(" ","")
    dic['其他信息']=i.find_all('p')[1].text.replace("\n","").replace(" ","")
    dic['简介']=i.find_all('p')[2].text.replace("\n","").replace(" ","")
    lis.append(dic)

df=pd.DataFrame(lis)
df.to_csv("dustin.csv")
print("succeed")
