from sqlalchemy.orm import Session
from .models import Fish

class FishRepository:
    @staticmethod
    def add(db: Session, fish_data: dict) -> Fish:
        new_fish = Fish(**fish_data)
        db.add(new_fish)
        db.commit()
        db.refresh(new_fish)
        return new_fish

    @staticmethod
    def get(db: Session, fish_id: int) -> Fish | None:
        return db.query(Fish).get(fish_id)

    @staticmethod
    def list(db: Session) -> list[Fish]:
        return db.query(Fish).all()

    @staticmethod
    def update(db: Session, fish_id: int, fish_data: dict) -> Fish | None:
        fish = db.query(Fish).get(fish_id)
        if fish is None:
            return None
        for key, value in fish_data.items():
            setattr(fish, key, value)
        db.commit()
        db.refresh(fish)
        return fish

    @staticmethod
    def delete(db: Session, fish_id: int) -> bool:
        fish = db.query(Fish).get(fish_id)
        if not fish:
            return False
        db.delete(fish)
        db.commit()
        return True
