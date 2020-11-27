import time
from pyperclip import paste as pw

out_path='d:/'
filename='note.txt'
outfile=out_path+filename
current_note=pw()
sepa='\n------------------------------------------------------------\n'
while True:
    note=pw()
    if note==current_note:
        pass
        time.sleep(2)
    else:
        try:
            with open(outfile,'a') as tar:
                tar.write(note+sepa)
            current_note=note
            print('当前笔记记录完毕，等待下一条笔记。。。。。。')
        except:
            pass

