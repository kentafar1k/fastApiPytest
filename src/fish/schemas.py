from pydantic import BaseModel, Field

class FishBase(BaseModel):
    name: str
    diet: str

class FishCreate(FishBase):
    pass

class FishSchema(FishBase):
    id: int

    def to_dict_wo_id(self):
        return self.model_dump(exclude={"id"})

    class Config:
        from_attributes = True  # для SQLAlchemy

