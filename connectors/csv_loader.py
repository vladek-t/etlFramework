import pandas as pd
import time

class CSVLoader():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            print(f"key: {key}, value: {value}")

    def extract(self):
        df = pd.read_csv(self.source_path)        
        return df

    def transform(self):
        df = self.extract()
        df['col4'] = df['col1'] + df['col3']
        return df

    def load(self):
        df = self.transform()
        df.to_csv(path_or_buf=self.target_path, index=False)
        print(f'File: csv2.csv has been created')

    def run(self):
        start = time.perf_counter()
        self.load()
        end = time.perf_counter()
        print(f"Время выполнения: {end - start} секунд")