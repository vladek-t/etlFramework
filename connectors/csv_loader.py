import pandas as pd
import time

class CSVLoader():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    # def __init__(self, path: str, encoding: str, delimiter: str):
    #     self.path = path

    def extract(self):
        df = pd.read_csv(self.path)        
        return df

    def transform(self):
        df = self.extract()
        df['col4'] = df['col1'] + df['col3']
        return df

    def load(self):
        df = self.transform()
        df.to_csv('files/csv2.csv', index=False)
        print(f'File: csv2.csv has been created')

    def run(self):
        start = time.perf_counter()
        self.load()
        end = time.perf_counter()
        print(f"Время выполнения: {end - start} секунд")