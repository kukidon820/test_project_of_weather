from sqlalchemy.future import select
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ..data.models import History
from ..data.create_engine import AsyncSessionLocal

router = APIRouter()
templates = Jinja2Templates(directory="client")


@router.get("/history/weather/", response_class=HTMLResponse)
async def get_weather_history(request: Request):
    """
    Возвращает страницу с историей запросов о погоде
    Args:
        request (Request): запрос от клиента
    Returns:
        HTMLResponse: страница history.html с историей запросов или сообщением об ошибке
    """
    browser_id = request.cookies.get("browser_id")

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(History).filter(History.browser_id == browser_id)
        )
        history = result.scalars().all()

        if not history:
            return templates.TemplateResponse(
                "history.html",
                {
                    "request": request,
                    "browser_id": browser_id,
                    "error_message": "Не получилось загрузить вашу историю! Перезагрузите страницу.",
                },
            )

        return templates.TemplateResponse(
            "history.html",
            {"request": request, "browser_id": browser_id, "history": history},
        )
