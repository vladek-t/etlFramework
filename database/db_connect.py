import sqlite3
from loguru import logger

class Database():
    def __init__(self, conn = 'database.db'):
        self.conn = sqlite3.connect(conn)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        logger.info(f"Подключение закрыто")