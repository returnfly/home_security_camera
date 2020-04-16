import requests
import json

# 消息中应包含 "home"

class Send_Message:
    def __init__ (self,text="home") :
        json_text = {
            "msgtype": "text",
            "at": {"atMobiles": ["11111"],"isAtAll": False},
            "text": {"content": text} }  

        token ="https://oapi.dingtalk.com/robot/send?access_token=7dfa2c07a7a181ef2ab36ad10298c9096dd658636734bd717893156cda0c7bb4"

        headers = {'Content-Type': 'application/json;charset=utf-8'}

        api_url = "https://oapi.dingtalk.com/robot/send?access_token=7dfa2c07a7a181ef2ab36ad10298c9096dd658636734bd717893156cda0c7bb4"

        print(requests.post(api_url, json.dumps(json_text), headers=headers).content)


if __name__ == '__main__':

    s_m = Send_Message("home-safe")


