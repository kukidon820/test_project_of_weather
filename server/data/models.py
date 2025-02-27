from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class History(Base):
    """
    модель для хранения истории запросов погоды

    Атрибуты:
        id (int): уникальный идентификатор записи
        browser_id (str): идентификатор браузера пользователя
        city_name (str): название города, по которому запрашивалась погода
        create_at (datetime): дата и время запроса.
        temperature (int, optional): температура в указанном городе
        humidity (float, optional): влажность в указанном городе
        weather_description (str, optional): описание погоды
    """

    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    browser_id = Column(String, index=True, nullable=False)
    city_name = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False)
    temperature = Column(Integer)
    humidity = Column(Float)
    weather_description = Column(String)

    def to_dict(self) -> dict:
        """
        преобразует объект модели в словарь

        Returns:
            dict: данные модели в формате словаря
        """
        return {
            "id": self.id,
            "browser_id": self.browser_id,
            "city_name": self.city_name,
            "create_at": self.create_at,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "weather_description": self.weather_description,
        }
