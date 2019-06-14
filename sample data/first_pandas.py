import pandas as pd
with open("operations.csv",'r',encoding='utf-8') as tar:
    for i in tar.readlines()[:7]:
        print(i.split(','))
f=open("operations.csv",'r',encoding='utf-8')
print(f)
