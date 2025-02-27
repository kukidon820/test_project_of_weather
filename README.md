Данное приложение разработано с использованием фреймворка FastAPI. Для взаимодействия с базой данных используется ORM SQLAlchemy с асинхронным драйвером asyncpg.
Для запуска приложения необходимо клонировать репозиторий https://github.com/kukidon820/test_project_of_weather, далее необходимо установить все зависимости при помощи команды: pip install -r requirements.txt
Также необходимо в корне проекта создать файл .env с переменными API_KEY (ключ для OpenWeatherMap) и DATABASE_URL (URL для подключения к базе данных). Пример: API_KEY=9dfeed7bdb0b4da392ea101aa21178db
                                                                                                                                                               DATABASE_URL=postgresql+asyncpg://weather_user:weather_pass@localhost/weather_db

Далее есть два варианта запуска приложения: 1) Перед запуском приложение запустите Postgresql. Запустите сервер FastAPI с помощью команды в терминале: uvicorn main:app --reload
                                            2) Запуск через Docker-compose(необходимо установить Docker engine). Чтоб запустить в терминале введите команду: docker-compose up -d и проверьте запущенные контейнеры при помощи команды dokcer ps

После запуска приложение будет доступно по следующим адресам:
        Главная страница: http://127.0.0.1:8000/get/weather/
        История запросов: http://127.0.0.1:8000/history/weather/    
        Так же можно посмотерть документацию: http://127.0.0.1:8000/docs
