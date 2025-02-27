from server.routes.main_route import router as main_route
from server.routes.history_route import router as history_route
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from server.data.create_engine import init_db

app = FastAPI()


@app.on_event("startup")
async def startup():
    await init_db()  # Вызываем init_db() при старте приложения


# Подключение маршрутов
app.mount("/static", StaticFiles(directory="client"), name="client")
app.include_router(main_route, prefix="")
app.include_router(history_route, prefix="")
