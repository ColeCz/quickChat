import psycopg

#NOTE: use async pool

def get_db_connection():
    # Using psycopg 3
    conn = psycopg.connect(
        host="localhost",
        dbname="messaging",
        user="your_user",
        password="your_password",
        autocommit=True  # optional, depends if you want autocommit
    )
    return conn