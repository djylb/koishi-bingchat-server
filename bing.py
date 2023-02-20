from EdgeGPT import Chatbot
from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()

HOST = "0.0.0.0"
PORT = 8007

chatbot = Chatbot(cookiePath='./cookie.json')
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
        await chatbot.reset()
        answer = "ERROR"
        pass
    flag = False
    return {"message": answer}

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
