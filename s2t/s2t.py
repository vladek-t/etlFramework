import getpass
import pandas as pd
from loguru import logger
import sys
import os
# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db_connect import Database


# username = getpass.getuser()
# print(username)

class LoadMetaData(Database):
    def __init__(self, file_path):
        super().__init__()
        logger.info(f"Подключение к БД установлено")

        self.file_path = file_path
    
    def print_file(self):
        df = pd.read_excel(self.file_path, 'loader_name')
        print(df)

# test = LoadMetaData('s2t.xlsx')
# test.print_file()