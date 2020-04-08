import time
import os
count=int(input('请输入现在持有的股票数量:'))
origin_price=float(input('请输入现在的股票价格:'))
profit=int(input('请输入现在的损益金额:'))
while True:
    target=float(input('请输入目标价格:'))
    print(int((target-origin_price)*count+profit))
    c=input('请按任意键继续')
    os.system('cls')
