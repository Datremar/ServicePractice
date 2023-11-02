from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:testpassword@localhost:5432/service_practice_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
