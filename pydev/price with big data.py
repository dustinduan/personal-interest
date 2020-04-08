import os
import time
import platform as pl
import tushare as ts

def clean_screen():
    if 'Windows' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")
met=input("请选择数据更新的方式:1.每10秒自动更新；2.手动按键更新\n")
def up_date(met):
    if met=='1':
        time.sleep(10)
        clean_screen()
    elif met=="2":
        c=input("请按任意键更新数据")
        clean_screen()

data=time.strftime("%Y-%m-%d",time.localtime())
stock=[]
with open('stock.txt','r') as source:
    for eachline in source:
        
        stock.append(eachline.strip('\n'))
while True:
    for i in stock:
        k=ts.get_realtime_quotes(i)
        print(k[['name','price','high','low','bid','ask']])
        k=ts.get_sina_dd(i,vol=500,date=data)
        try:
            print(k[['name','code','time','price','volume','type']].loc[0:5])
        except:
            print("No big Data.")
    up_date(met)
