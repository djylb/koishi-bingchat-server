# 如需使用代理功能请取消注释并按需要修改
#import os
#os.environ["http_proxy"] = "http://127.0.0.1:8080"
#os.environ["https_proxy"] = "http://127.0.0.1:8080"

import traceback
from EdgeGPT import Chatbot
from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()

# 手动配置时按需要修改监听地址和端口
HOST = "0.0.0.0"
PORT = 8007

# 手动配置时按需要修改cookie文件路径，将./cookie.json修改为你自己的文件位置（一般不用修改）
chatbot = Chatbot(cookie_path='./cookies.json')
flag = False


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.post("/bing")
async def chatGPT(body: dict = Body(...)):
    global flag
    prompt = body["prompt"]
    print("User: " + prompt)

    if flag:
        return {"message": "接口繁忙，请稍后再试。"}

    try:
        flag = True
        if prompt == "!reset":
            await chatbot.reset()
            print("OK")
            flag = False
            return {"message": "OK"}
        answer = (await chatbot.ask(prompt))["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"]
        print("Bingbot: " + answer)
    except:
        traceback.print_exc()
        await chatbot.reset()
        answer = "ERROR"
        pass
    flag = False
    return {"message": answer}

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
