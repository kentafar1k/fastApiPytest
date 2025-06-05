from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .schemas import FishCreate, FishSchema
from .service import FishService

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


# Создаём таблицы в БД
Base.metadata.create_all(bind=engine)

# Зависимость: получить сессию БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fish/", response_model=FishSchema)
def create_fish(fish: FishCreate, db: Session = Depends(get_db)):
    return FishService.add(db, fish)

@app.get("/fish/", response_model=list[FishSchema])
def list_fish(db: Session = Depends(get_db)):
    return FishService.list(db)

@app.get("/fish/{fish_id}", response_model=FishSchema)
def get_fish(fish_id: int, db: Session = Depends(get_db)):
    fish = FishService.get(db, fish_id)
    if fish is None:
        raise HTTPException(status_code=404, detail="Fish not found")
    return fish

@app.put("/fish/{fish_id}", response_model=FishSchema)
def update_fish(fish_id: int, fish: FishCreate, db: Session = Depends(get_db)):
    updated = FishService.update(db, fish_id, fish)
    if updated is None:
        raise HTTPException(status_code=404, detail="Fish not found")
    return updated

@app.delete("/fish/{fish_id}")
def delete_fish(fish_id: int, db: Session = Depends(get_db)):
    success = FishService.delete(db, fish_id)
    if not success:
        raise HTTPException(status_code=404, detail="Fish not found")
    return {"message": "Fish deleted successfully"}

