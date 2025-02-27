from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import patch
from routes.main_route import router
import pytest


app = FastAPI()
app.include_router(router)

client = TestClient(app)


@pytest.mark.asyncio
async def test_get_weather_page():

    response = client.get("/get/weather/")

    assert response.status_code == 200
    assert b'<form method="post" action="/get/weather/info/"' in response.content


@pytest.mark.asyncio
async def test_post_weather_info_success():
    mock_weather_data = {
        "weather_description": "clear sky",
        "temperature": 15,
        "humidity": 60,
    }

    with patch(
        "functions_with_api_weather.get_data_by_name_city.get_weather",
        return_value=mock_weather_data,
    ):
        response = client.post("/get/weather/info/", data={"city": "Minsk"})

    assert response.status_code == 200

    assert b"clear sky" in response.content
    assert b"15" in response.content
    assert b"60" in response.content
