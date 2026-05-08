import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        host="136.114.103.245",
        database="vapp_db",
        user="vapp_user",
        password=os.environ.get("DB_PASSWORD"),
        port=5432
    )