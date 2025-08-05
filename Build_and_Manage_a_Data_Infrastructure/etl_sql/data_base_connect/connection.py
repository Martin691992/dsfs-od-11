import mysql.connector as sql
from dotenv import load_dotenv
import os

class Connector():
    def __init__(self):
        load_dotenv()
        self.connector = sql.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = self.connector.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ")




