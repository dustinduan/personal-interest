import requests as rq
import json
import time

def tranlate(source, direction="auto2zh"):
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    #WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "nf9crqcegq6ydveip08r"
    payload={
            "source" : source,
            "trans_type" : direction,
            "request_id" : "demo",
            "detect": True,
            }
    headers={
            'content-type': "application/json",
            'x-authorization': "token " + token,
            }
    response=rq.request("POST", url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)['target']
print("选择1：翻译成中文\n")
print("选择2：翻译成英语\n")
print("选择3：翻译成日语\n")
c=input("请输入你的选择1/2/3：")
choice={"1":"auto2zh","2":"auto2en","3":"auto2ja"}
while True:
    try:
        source=input('请输入需要翻译的句子或者单词:')
        k=tranlate(source,direction=choice[c])
        print(k)
        with open('d:/translation_rec.txt','a') as tar:
            tar.write("翻译前:"+source+'\n'+"翻译后:"+k+'\n')
    except:
        print('翻译失败，请继续尝试。。。')

