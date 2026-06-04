from sqlalchemy import create_engine, text
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)
import time

DATABASE_URL = (
    "postgresql://postgres:"
    "password123@db:5432/"
    "personal_cloud"
)


def get_engine_with_retry(
    retries=10,
    delay=2
):
    for i in range(retries):
        try:
            engine = create_engine(
                DATABASE_URL,
                pool_pre_ping=True
            )

            connection = engine.connect()
            connection.close()

            return engine

        except Exception:
            print(
                f"DB not ready, retrying "
                f"({i + 1}/{retries})..."
            )

            time.sleep(delay)

    raise Exception(
        "Database connection failed "
        "after retries"
    )


engine = get_engine_with_retry()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()