import string
white_char=string.punctuation
word=dict()
def charana(s):#直方图函数
        for c in s:
            if c in white_char:
                pass
            elif c in word:
                word[c]+=1
            else:
                word[c]=1

with open('pg60713.txt','r') as sou:
    for eachline in sou:
        stre=eachline.strip('\n').strip(' ').split(' ')
        charana(stre)
for i in word:
    print(i,word[i],'\n')
