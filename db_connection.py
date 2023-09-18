import psycopg2

# Connect to db
conn = psycopg2.connect(
    dbname="todo",
    user="postgres",
    password="Qwerty512228",
    host="localhost",  # Или другой адрес сервера PostgreSQL
    port="5432",
)

# Create cursor
cursor = conn.cursor()
