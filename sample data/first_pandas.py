import pandas as pd
with open("operations.csv",'r',encoding='utf-8') as tar:
    for i in tar.readlines()[:5]:
        print(i.split(','))
