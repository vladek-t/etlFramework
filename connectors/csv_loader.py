"""
Загрузчик CSV
"""

import pandas as pd
from connectors.dataloader import DataLoader
from connectors.registry_connectors import register_loaders
from loguru import logger

class CSVLoader(DataLoader):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            logger.info(f"key: {key}, value: {value}")

    def extract(self):
        self.df = pd.read_csv(
            self.source_path, 
            delimiter=self.delimiter,
            encoding=self.encoding
        )

    def transform(self):
        self.df['col4'] = self.df['col1'] + self.df['col3']

    def load(self):
        self.df.to_csv(
            path_or_buf=self.target_path, 
            index=False,
            sep=self.delimiter,
            encoding=self.encoding
        )
        logger.info(f'File: {self.target_path} has been created')

# Автоматическая регистрация при импорте
register_loaders(
    name='csv',
    loader_class=CSVLoader,
    required_params=['source_path', 'target_path'],
    optional_params={'delimiter': ',', 'encoding': 'utf-8'}
)