import psycopg
import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME")

def read_sql_file(path: str) -> List[str]:
    with open(path, "r") as f:
        sql_content = f.read()
    statements = [stmt.strip() for stmt in sql_content.split(";") if stmt.strip()]
    return statements

def run_schema():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(base_dir, "..", "..", "database")

    create_schema_sql_statements = read_sql_file(
        os.path.join(db_dir, "02-create-schema.sql")
    )

    conninfo_target = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

    with psycopg.connect(conninfo_target, autocommit=True) as conn:
        with conn.cursor() as cur:
            for stmt in create_schema_sql_statements:
                cur.execute(stmt)

    print("####### Schema Initialized #######")

if __name__ == "__main__":
    run_schema()
