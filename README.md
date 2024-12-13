# Factory's cables management app

Веб-приложени для поиска, учета выдачи и отслеживания сроков проверки кабелей.

## Описание

Функционал приложения:
 - поиск кабелей по индексу, группе, сборке и заводскому номуру;
 - автоматическое отслеживание сроков проверки кабелей;
 - учет выдачи кабелей по qr-коду;  # В разработке
 - генерация уникального qr-кода сотрудника;  # В разработке
 - логирование операций выдачи/возврата кабелей с записью в файл;  # В разработке
 - система аутенификации и авторизации;
 - личный кабинет работника;
 - панель администратора;  # В разработке
 - автоматический бэкап базы данных(БД) по таймеру;
 - простой интерфейс для восстановления БД из бэкапа.  # В разработке

Информация предствляемая пользователям:
 - статус кабеля (наличии/выдан);
 - сроки проверки (текущая/следущая проверка);
 - информация о получателе (ФИО; подразделение; номер телефона);
 - список каблей, полученных работником;
 - дата получения кабеля;
 - история операций;  # В разработке
 - ФИО работника кладовой выдавшего кабель.

Технические особенности приложения:
 - Асинхронный, быстрый фреймворк выдерживающий большие нагрузки;
 - Реляционная база данных выдерживающая большие нагрузки;
 - Кэширование популярных запросов;
 - Архитектура приложения с разделением позволяющая легко масштабировать проект;
 - Запись метрик для анализа производительности;  # В разработке
 - Поддержка фоновых задач;
 - Запуск из docker контейнеров, что позволяет быстро развернуть приложение на других машинах.

Технлогический стек:
 - FastAPI;
 - PostgreSQL;
 - Redis;
 - Celery;
 - Docker;
 - RabbitMQ;  # В разработке
 - Prometeus;  # В разработке
 - Grafana;  # В разработке

## Установка

Для установки и запуска проекта требуется наличие программ Git и Docker на компьютере. 

Следуйте этим шагам, чтобы установить проект:

1. Клонируйте репозиторий:

   `git clone https://github.com/opletaev/Digital_cable_storage.git`
   `cd Digital_cable_storage`

2. Для установка и запуск приложения:

   `docker compose up --build`

Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000 для доступа к приложению.

## API Документация

Вы можете получить доступ к документации по следующим адресам:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
