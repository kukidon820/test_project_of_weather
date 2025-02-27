from datetime import datetime
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ..data.models import History
from ..data.create_engine import AsyncSessionLocal
from ..functions_with_api_weather.get_data_by_name_city import get_weather
from ..set_cookies import ensure_browser_id

router = APIRouter()
templates = Jinja2Templates(directory="client")


@router.get("/get/weather/", response_class=HTMLResponse)
async def get_weather_page(request: Request):
    """
    Возвращает HTML-страницу с формой для запроса погоды
    Args:
        request (Request): запрос от клиента
    Returns:
        HTMLResponse: главная страница с полем ввода города
    """
    response = templates.TemplateResponse("main.html", {"request": request})
    await ensure_browser_id(request, response)
    return response


@router.post("/get/weather/info/", response_class=HTMLResponse)
async def post_weather(
    request: Request, city: str = Form(..., description="City name")
):
    """
    Обрабатывает форму с названием города и возвращает данные о погоде
    Args:
        request (Request): запрос от клиента
        city (str): название города, введенное пользователем
    Returns:
        HTMLResponse: страница с информацией о погоде или сообщением об ошибке
    """
    response = templates.TemplateResponse("main.html", {"request": request})
    browser_id = await ensure_browser_id(request, response)

    async with AsyncSessionLocal() as session:
        data = await get_weather(city)
        if data:
            history = History(
                browser_id=browser_id,
                city_name=city,
                create_at=datetime.now(),
                temperature=data.get("temperature"),
                humidity=data.get("humidity"),
                weather_description=data.get("weather_description"),
            )
            session.add(history)
            await session.commit()
            return templates.TemplateResponse(
                "main.html",
                {
                    "request": request,
                    "browser_id": browser_id,
                    "data": data,
                    "city_name": city,
                },
            )
        return templates.TemplateResponse(
            "main.html",
            {
                "request": request,
                "browser_id": browser_id,
                "error_message": "Не удалось получить данные о погоде в этом городе!",
            },
        )
