import requests as rq
from bs4 import BeautifulSoup as bp
import itertools as it
def qidian_fengtui_list(url):
    r=rq.get(url)
    soup=bp(r.text,'lxml')
    lst=soup.find_all('a')
    with open('fengtui.txt','a',encoding='utf-8') as tar:
        for i in lst:
            if "book.qidian.com" in i.attrs['href']:
                if i.text=='':
                    pass
                else:
                    tar.write(i.text+'\n')
                    print(i.text)
for page in it.count(1):
    url="https://www.qidian.com/book/coverrec?page=%d" % page
    qidian_fengtui_list(url)
    if page>30:
        break
print('数据收集完毕。')
