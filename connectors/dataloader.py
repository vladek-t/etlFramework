from abc import ABC, abstractmethod
import time
from loguru import logger

class DataLoader(ABC):    
    @abstractmethod
    def extract(self):
        pass

    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass

    def run(self):
        start = time.perf_counter()
        self.extract()
        self.transform()
        self.load()
        end = time.perf_counter()
        logger.info(f"Время выполнения: {end - start} секунд")