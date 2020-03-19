import os
def stock_research(stock_code):
    os.system('cls')
    main_power_profit=input('请输入主力目前的损益比例:')
    trend_control=input('请输入目前的主力控盘坚决度:')
    trend_daily=input('请确认目前是否呈现多头排列:')
    main_price=input('请输入目前的主力成本:')
    with open('research.txt','a') as tar:
        tar.write(stock_code+' '+main_price+' '+main_power_profit+' '+trend_control+' '+trend_daily+'\n')
while True:
    code=input('请输入需要调查和记录的股票代码:')
    stock_research(code)
