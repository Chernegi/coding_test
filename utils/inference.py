import typing as t
from abc import ABC
from pydantic import BaseModel


class Message(BaseModel):
    message: str


class BaseInfetence(ABC):
    async def get_response(self, msg: Message) -> t.Dict[str, str]:
        raise NotImplementedError
    

class EchoInference(BaseInfetence):
    async def get_response(self, msg: Message) -> t.Dict[str, str]:
        return {"echo": "Hello world"}
