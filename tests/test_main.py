import pytest
from contextlib import nullcontext as does_not_raise

from src.fish.schemas import FishSchema, FishBase
from src.fish.service import FishService
from src.fish.models import Fish
from sqlalchemy.orm import Session
from src.fish.database import Base, engine

from src.fish.main import Calculator


# pytest tests/test_main.py::TestCalculator::test_divide -v
# pytest tests/test_main.py::TestFish -v

@pytest.fixture(scope='function', autouse=True)  # автоюз типо автоматически используй фикстуру в тестах
def setup_db():
    print("Перед созданием бд")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("После созданием бд")




@pytest.fixture
def fishes(db):
    fish_data = [
        FishBase(name="fish1", diet="predator"),
        FishBase(name="fish2", diet="predator"),
        FishBase(name="fish3", diet="predator"),
    ]
    for fish in fish_data:
        FishService.add(db, fish)
    return fish_data

@pytest.fixture(scope="function", autouse=True)
def empty_fishes(db):
    FishService.delete_all(db)


class TestFish:
    def test_count_fish(self, db, fishes, empty_fishes):
        assert FishService.count(db) == 3

