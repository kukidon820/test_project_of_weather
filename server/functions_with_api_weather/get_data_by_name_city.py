import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()


async def get_weather(city: str):
    """
    Получает данные о погоде по названию города с API OpenWeather
    Args:
        city (str): название города
    Returns:
        dict: данные о погоде (описание, температура, влажность) или None в случае ошибки
    """
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("API-ключ отсутствует в файле .env!")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "weather_description": data["weather"][0]["description"],
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                }
            return None
