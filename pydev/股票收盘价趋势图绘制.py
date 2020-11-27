import tushare as ts
import time

start_date=input('请输入查询股票信息的起始日期:')
end_date=input('请输入查询股票信息的结束日期:')

def close_trend(start_date,end_date):
    code=input('请输入需要查询的股票代码:')
    df=ts.get_k_data(code=code,start=start_date,end=end_date)
    #df.head()
    df.set_index('date',inplace=True)
    df['close'].plot()
        
close_trend(start_date,end_date)
c=input('请按任意键结束......')

