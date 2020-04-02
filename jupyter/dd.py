import wget
import os
import time

def getfile(filename):
    wget.download(filename)

website=input("请输入需要下载的网络文件的完整地址:")
getfile(website)
print("文件下载完成。。。。。。")
time.sleep(10)
