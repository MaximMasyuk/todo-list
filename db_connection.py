import psycopg2
from decouple import config

# Подключение к базе данных
conn = psycopg2.connect(
    dbname=config("DATABASE_NAME"),
    user=config("DATABASE_USER"),
    password=config("DATABASE_PASSWORD"),
    host=config("DATABASE_HOST"),  # Или другой адрес сервера PostgreSQL
    port=config("DATABASE_PORT")
)

# Создание курсора
cursor = conn.cursor()
