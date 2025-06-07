from typing import Optional
from pydantic import TypeAdapter
from sqlalchemy.orm import Session

from .schemas import FishSchema, FishCreate
from .repository import FishRepository

class FishService:
    @classmethod
    def add(cls, db: Session, fish: FishCreate) -> dict:
        fish_dict = fish.model_dump()
        new_fish = FishRepository.add(db, fish_dict)
        return TypeAdapter(FishSchema).dump_python(new_fish)

    @classmethod
    def get(cls, db: Session, fish_id: int) -> Optional[dict]:
        fish = FishRepository.get(db, fish_id)
        if not fish:
            return None
        return TypeAdapter(FishSchema).dump_python(fish)

    @classmethod
    def list(cls, db: Session) -> list[dict]:
        fishes = FishRepository.list(db)
        return TypeAdapter(list[FishSchema]).dump_python(fishes)

    @classmethod
    def update(cls, db: Session, fish_id: int, fish: FishCreate) -> Optional[dict]:
        fish_dict = fish.model_dump()
        updated_fish = FishRepository.update(db, fish_id, fish_dict)
        if not updated_fish:
            return None
        return TypeAdapter(FishSchema).dump_python(updated_fish)

    @classmethod
    def delete(cls, db: Session, fish_id: int) -> bool:
        return FishRepository.delete(db, fish_id)

    @classmethod
    def delete_all(cls, db: Session):
        return FishRepository.delete_all(db)

    @classmethod
    def count(cls, db: Session) -> int:
        return FishRepository.count(db)