from fastapi import Request
import uuid


async def ensure_browser_id(request: Request, response) -> str:
    """
    Проверяет наличие идентификатора браузера в cookie, если его нет — создает новый
    Args:
        request (Request): запрос пользователя
        response: ответ, в который будет установлена cookie
    Returns:
        str: идентификатор браузера
    """
    browser_id = request.cookies.get("browser_id")
    if not browser_id:
        browser_id = str(uuid.uuid4())
        response.set_cookie(
            key="browser_id",
            value=browser_id,
            max_age=36000000,
            httponly=True,
            secure=False,
            path="/",
            samesite="lax",
        )
    return browser_id
