from fastapi import FastAPI
from utils.inference import EchoInference, Message


app = FastAPI()
inference = EchoInference()


#TODO: implement the echo chatbot
@app.post("/echo")
async def echo_message(msg: Message):
    return await inference.get_response(msg) 
