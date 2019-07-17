import requests as req
from bs4 import BeautifulSoup as bup
import pandas as pd
def biquge_page_get(web_address):
    u=req.get(url=web_address)
    soup=bup(u.text,'lxml')
    print(soup)

web_add=input('请输入小说的首页地址:\n')
biquge_page_get(web_add)
