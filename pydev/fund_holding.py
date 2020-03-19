import tushare as ts
df=ts.fund_holdings(2019,4)
print(df)
df.to_excel('fund.xlsx')