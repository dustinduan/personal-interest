import tushare as ts
import os
while True:
    df=ts.guba_sina()
    print(df)
    c=input("按任意键更新")
    os.system('cls')