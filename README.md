# Запуск

docker compose up -d

# Миграции базы данных:

docker compose exec auth_service alembic revision --autogenerate -m "Migration"
docker compose exec auth_service alembic upgrade head

# Работа с работающим докером

docker compose down -v
docker compose ps

docker compose logs -f
docker compose logs kafka

# Kafka

### Список топиков
docker compose exec kafka kafka-topics --list --bootstrap-server kafka:9092

### Создать топик
docker compose exec kafka kafka-topics --create --topic notifications --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092

# Локальная разработка

### Auth Service
cd auth_service
uvicorn app.main:app --reload --port 8000

### Notification Service
cd notification_service
uvicorn main:app --reload --port 8001