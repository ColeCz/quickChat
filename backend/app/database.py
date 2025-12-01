import psycopg
import os
from psycopg_pool import ConnectionPool
from dotenv import load_dotenv


load_dotenv()
conninfo = "postgresql://" + os.getenv("DB_USER") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv("DB_HOST") + ":" + os.getenv("DB_PORT") + "/" + os.getenv("DB_NAME")

pool = ConnectionPool(
    conninfo,
    max_size=5,
)