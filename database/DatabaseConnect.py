"""
Файл подключения к БД, передает необходимые атрибуты в наследуемые классы
"""

from loguru import logger
import psycopg2
from DatabaseConfig import PG_DBNAME, PG_PASSWORD, PG_PORT, PG_USER, PG_HOST

class Database():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host=PG_HOST,
                port=PG_PORT,
                database=PG_DBNAME,
                user=PG_USER,
                password=PG_PASSWORD
            )
        except psycopg2.OperationalError:
            raise ValueError(f"Unable to connect to the database, please check the correctness of the entered data.")
        
        self.cursor = self.conn.cursor()
        logger.info("Подключение к БД установлено")
        
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        logger.info(f"Подключение закрыто")