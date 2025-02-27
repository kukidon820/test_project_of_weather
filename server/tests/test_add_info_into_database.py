from .conftest import History
import uuid
from datetime import datetime


def test_add_weather(db_session):
    browser_id = str(uuid.uuid4())
    # Проверяю добавление данных в таблицу
    new_weather = History(
        browser_id=browser_id,
        city_name="Minsk",
        create_at=datetime.now(),
        temperature=20,
        humidity=20.5,
        weather_description="Normal",
    )
    db_session.add(new_weather)
    db_session.commit()

    weather = db_session.query(History).filter_by(city_name="Minsk").first()

    assert weather is not None
    assert weather.city_name == "Minsk"
    assert weather.temperature == 20
    assert weather.humidity == 20.5
    assert weather.weather_description == "Normal"
