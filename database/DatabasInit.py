from database.DatabaseConnect import Database
from loguru import logger

class InitDatabase(Database):
    def __init__(self):
        super().__init__()
        logger.info(f"Подключение к БД установлено")

    def create_meta_table(self, file_path='sql/create_table.sql'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                sql_script = f.read()
            self.cursor.executescript(sql_script)
            self.conn.commit()
            logger.info(f"SQL-скрипт {file_path} выполнен успешно")
        except Exception as e:
            logger.error(f"Ошибка при выполнении скрипта {file_path}: {e}")
            raise
    
    def drop_meta_table(self, file_path='sql/drop_table.sql'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                sql_script = f.read()
            self.cursor.executescript(sql_script)
            self.conn.commit()
            logger.info(f"SQL-скрипт {file_path} выполнен успешно")
        except Exception as e:
            logger.error(f"Ошибка при выполнении скрипта {file_path}: {e}")
            raise
    
    def run(self):
        self.create_meta_table()
        self.close_connection()