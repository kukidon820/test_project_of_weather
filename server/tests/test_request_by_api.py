import os
from dotenv import load_dotenv
import pytest
from aioresponses import aioresponses
from functions_with_api_weather.get_data_by_name_city import get_weather

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API-ключ отсутствует в файле .env!")


@pytest.mark.asyncio
async def test_get_weather_success():
    city = "Minsk"

    # Использую имитацию данных, чтоб тест прошел успешно
    mock_response = {
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 15, "humidity": 60},
    }

    with aioresponses() as m:
        m.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric",
            payload=mock_response,
        )

        result = await get_weather(city)

    assert result is not None
    assert result["weather_description"] == "clear sky"
    assert result["temperature"] == 15
    assert result["humidity"] == 60
