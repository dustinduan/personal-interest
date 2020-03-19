import time
from pyperclip import paste as pw

current_note=pw()
sepa='------------------------------------------------------------\n'
while True:
    note=pw()
    if note==current_note:
        pass
        time.sleep(2)
    else:
        try:
            with open('note.txt','a') as tar:
                tar.write(sepa+note+sepa)
            current_note=note
            print('当前笔记记录完毕，等待下一条笔记。。。。。。')
        except:
            pass

