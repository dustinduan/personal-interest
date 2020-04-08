import wget
import time
from pyperclip import paste as pw

current_url=pw()
while True:
    url=pw()
    if url==current_url:
        pass
        time.sleep(2)
    else:
        try:
            print(url.split('/')[-1])
            wget.download(url,url.split('/')[-1])
            current_url=url
            print('当前文件下载完毕，等待下一条链接。。。。。。')
        except:
            try:
                with open('note.txt','a') as tar:
                    tar.write(sepa+url+sepa)
                    current_url=url
                    print('当前笔记记录完毕，等待下一条笔记。。。。。。')
            except:
                pass
