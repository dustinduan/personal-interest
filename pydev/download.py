import time
from pyperclip import paste as pw
import wget

current_note=pw()
while True:
    note=pw()
    if note==current_note:
        pass
        time.sleep(2)
    else:
        try:
            wget.download(note)
        except:
            print('下载失败，尝试重新下载。。。。。。')
            current_note=None
