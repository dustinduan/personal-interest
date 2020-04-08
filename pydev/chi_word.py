import jieba

def word_diff():
    result=jieba.cut(input('请输入需要拆分词语的句子:'),cut_all=True)
    for word in result:
        print(word)

word_diff()
