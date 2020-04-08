import os
c=input("请输入需要记录内容的为游戏名称:(1.游戏记录 2.笔记 3.网络地址)")
choice={'1':'游戏记录.txt','2':'note.txt','3':'netaddress.txt'}
target_file=choice[c]
os.system('cls')
def game_rec(gamefile=choice):
    info=input('请输入需要记录的内容:')+'\n'
    with open(gamefile,'a') as tar:
        tar.write(info)

def net_rec(rec=choice):
    info=input('请输入需要记录的内容:')+'\n'
    index=input('请输入记录的标题:')
    with open(rec,'a') as tar:
        tar.write(index+'\n'+info)

def note_rec(rec=choice):
    info=input('请输入需要记录的内容:')+'\n'
    with open(rec,'a') as tar:
        tar.write(info)
while True:
    if c=='1':
        game_rec(target_file)
    elif c=='2':
        note_rec(target_file)
    else:
        net_rec(target_file)
    
