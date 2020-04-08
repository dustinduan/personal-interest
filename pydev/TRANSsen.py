import requests as rq
import json
import os
import time

def tranlate(source, direction="auto2zh"):    
    url = "http://api.interpreter.caiyunai.com/v1/translator"
    #WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "3975l6lr5pcbvidl6jl2"
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
    
def sen():
    k=''
    source=[]
    if os.path.exists('english.txt'):
        try:
            with open('english.txt','r') as sou:
                for eachline in sou:
                    source.append(eachline.strip('\n'))
            for i in source:
                k=k+i
            print(tranlate(k))
            os.remove('english.txt')
            time.sleep(10)
        except:
            pass
    else:
        pass

while True:
    sen()

