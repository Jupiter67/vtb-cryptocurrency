# vtb-cryptocurrency

Сервис работы с криптокошельками и транзакциями

## Конфигурация

Пример конфигурации есть в файле `settings.yaml.copy`

`host`              - адрес сервиса

`port`              - порт сервиса

`vtb_private_key`   - приватный ключ "кошелька-банка"

`vtb_public_key`    - публичный ключ "кошелька-банка"

`pg_host`           - адрес сервера PostgresQL

`pg_port`           - порт сервера PostgresQL

`pg_user`           - пользователь на сервере PostgresQL

`pg_password`       - пароль пользователя сервере PostgresQL

`pg_database`       - название базы данных на сервере PostgresQL

## Запуск

### Docker

```bash
docker-compose up --build
```

### Без контейнера

```bash
python3 -m venv env
source env/bin/activate
pip install -U pip
pip install -r requirements.txt
alembic upgrade head
python3 main.py
```

## Документация

По адресу `host:port/docs` можно посмотреть документацию API (Swagger).