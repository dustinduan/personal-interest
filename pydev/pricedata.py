import requests as rq
from bs4 import BeautifulSoup as bp
import itertools as it
url='http://www.100ppi.com/mprice/mlist-1.html'
r=rq.get(url)
soup=bp(r.text,'lxml')
print(soup)
