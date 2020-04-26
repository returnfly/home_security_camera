# 此页需要修改

import requests
import json

# text中填入需要包含的关键字，发送消息中应包含 text,否则发送失败
# token和api_url填入的皆为钉钉机器人返回的Webhook 地址

class Send_Message:
    def __init__ (self,text="xxxx") :
        json_text = {
            "msgtype": "text",
            "at": {"atMobiles": ["11111"],"isAtAll": False},
            "text": {"content": text} }  

        token ="xxxx"

        headers = {'Content-Type': 'application/json;charset=utf-8'}

        api_url = "xxxx"

        print(requests.post(api_url, json.dumps(json_text), headers=headers).content)


# 此处需要填入想要发送的消息，注意消息中应包含前边设置的关键字
if __name__ == '__main__':

    s_m = Send_Message("xxxx")


