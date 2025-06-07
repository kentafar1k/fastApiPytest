# tests/conftest.py или tests/test_main.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.fish.database import Base
from src.fish.models import Fish  # Обязательно импортируй модель, чтобы Base её "знал"

# Используем in-memory SQLite для тестов
TEST_DATABASE_URL = "sqlite:///:memory:"

# Создаём движок и сессию
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Фикстура для базы данных
@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)  # создаём таблицы
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # удаляем таблицы после теста
