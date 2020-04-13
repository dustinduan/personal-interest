import xlwt,xlrd
import pandas as pd
import os

def ex_combin():
    in_path=input('请输入需要汇总的excel文件的路径:')
    out_path=input('请输入汇总结果的文件的保存路径:')
    new_name=input('请输入汇总结果保存的文件名称:')+'.xlsx'
    file_list=os.listdir(in_path)
    df=[]
    try:
        for i in file_list:
            df.append(pd.read_excel(in_path+i))
            print('%s完成汇总',(i))
        result=pd.concat(df)
        k=result.drop_duplicates()
        print(k)
        k.to_excel(out_path+new_name)
    except:
        print('文件汇总失败，请检查文件后重新尝试.')

ex_combin()