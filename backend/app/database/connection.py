import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy import text

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "pathwise")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")

database_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME,
)

engine = create_engine(database_url)



with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print("Database connection successful:", result.scalar())