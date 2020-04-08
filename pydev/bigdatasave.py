import pandas as pd
import matplotlib as plt
import time
import os
def big_data_save():
    super_data=input('请输入特大单的数量:')
    big_data=input('请输入大单数量:')
    final_data=str(int(super_data)+int(big_data))
    with open('big.txt','a') as tar:
        tar.write(super_data+','+big_data+','+final_data+'\n')
    with open('big.txt','r') as sou:
        for eachline in sou:
            print(eachline.strip('\n'))
while True:
    big_data_save()
    
