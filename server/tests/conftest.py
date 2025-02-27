import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

DATABASE_URL = (
    "postgresql://test_weather_user:test_weather_pass@localhost:5432/test_weather_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class History(Base):

    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    browser_id = Column(String, index=True, nullable=False)
    city_name = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False)
    temperature = Column(Integer)
    humidity = Column(Float)
    weather_description = Column(String)


@pytest.fixture(scope="function")
def db_session():
    """Фикстура для создания и удаления таблиц в базе"""
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(bind=engine)
