import time
from sqlalchemy import text
from app.db.database import engine

def wait_for_db(retries=10):
    for i in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("DB is ready")
            return
        except Exception as e:
            print(f"DB not ready yet ({i+1}/{retries})")
            time.sleep(2)

    raise Exception("Database never became ready")
