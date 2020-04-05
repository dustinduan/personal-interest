import time
from pyperclip import paste as pw
import wget

out_path='D:/360Downloads/'
current_note=pw()
while True:
    note=pw()
    if note==current_note:
        pass
        time.sleep(2)
    else:
        try:
            wget.download(note,out=out_path+note.split('/')[-1])
            current_note=note
        except:
            print('下载失败')
            current_note=note
