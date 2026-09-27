# Product Shop

Простой магазин продуктов на FastAPI + PostgreSQL. Реализованы только CRUD операции над товарами.

## Стек

- FastAPI
- SQLAlchemy (async) + asyncpg
- PostgreSQL
- Docker + Docker Compose

## Структура проекта

```
.
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── modules/
│   │   └── products/
│   │       ├── models.py
│   │       ├── router.py
│   │       ├── schemas.py
│   │       └── service.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── requirements.txt
```

## Запуск

1. Скопировать `.env.example` в `.env` (при необходимости поменять значения):

   ```bash
   cp .env.example .env
   ```

2. Собрать и запустить контейнеры:

   ```bash
   docker compose up -d --build
   ```

3. API доступно по адресу `http://localhost:8000`, Swagger — `http://localhost:8000/docs`.

## API

| Метод  | Путь                   | Описание             |
|--------|------------------------|----------------------|
| GET    | /api/v1/products       | Список товаров       |
| GET    | /api/v1/products/{id}  | Получить товар по id |
| POST   | /api/v1/products       | Создать товар        |
| PUT    | /api/v1/products/{id}  | Обновить товар       |
| DELETE | /api/v1/products/{id}  | Удалить товар        |

Тело запроса для создания и обновления:

```json
{
  "name": "Apple",
  "price": 1.5,
  "stock": 100
}
```

## Примеры запросов

```bash
curl -X POST http://localhost:8000/api/v1/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Apple","price":1.5,"stock":100}'

curl http://localhost:8000/api/v1/products

curl http://localhost:8000/api/v1/products/1

curl -X PUT http://localhost:8000/api/v1/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Green Apple","price":2.0,"stock":50}'

curl -X DELETE http://localhost:8000/api/v1/products/1
```

## Остановка

```bash
docker compose down
```

Чтобы дополнительно удалить данные базы:

```bash
docker compose down -v
```
