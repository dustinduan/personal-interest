import tushare as ts

out_path='d:/result/stock/'
filetype='.xlsx'

year=int(input('请输入财报的年份数字:'))
season=int(input('请输入财报的季度数字:'))

df=ts.get_stock_basics()
filename='stockinfo'
print('正在下载股票代码......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.get_report_data(year,season)
filename='mainreport'
print('正在下载主要报表......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.get_profit_data(year,season)
filename='profit'
print('正在下载利润表......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.get_operation_data(year,season)
filename='management'
print('正在下载营运报表......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.get_growth_data(year,season)
filename='growth'
print('正在下载成长性报表......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.get_debtpaying_data(year,season)
filename='debt'
print('正在下载资产负债表......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.get_cashflow_data(year,season)
filename='cashflow'
print('正在下载现金流量表......\n')
df.to_excel(out_path+filename+filetype)
print('\n')

df=ts.fund_holdings(year,season)
filename='基金持股数据'
print('正在下载基金持股数据......\n')
df.to_excel(out_path+filename+filetype)
print('\n')
