from fastapi import FastAPI
from typing import Union

app = FastAPI()


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if not isinstance(x, (int, float)) or not isinstance(y, (int,float)):
            raise TypeError("x and y must be integers or floats")
        if y == 0:
            raise ZeroDivisionError("на нуль делить нельзя")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        if not isinstance(x, (int, float)) or not isinstance(y, (int,float)):
            raise TypeError("x and y must be integers or floats")
        return x + y


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

