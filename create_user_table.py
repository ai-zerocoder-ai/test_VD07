from app import app, db
from sqlalchemy import Table, Column, Integer, String, MetaData

# Создаём объект MetaData
metadata = MetaData()

# Определяем таблицу user
user_table = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), nullable=False, unique=True),
    Column('email', String(120), nullable=False, unique=True),
    Column('password', String(60), nullable=False)
)

# Устанавливаем контекст приложения
with app.app_context():
    # Создаём таблицу
    engine = db.engine
    metadata.create_all(engine)
    print("Таблица 'user' успешно создана!")
