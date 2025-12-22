import pandas as pd

class SimpleETL():
    def extract(self, path, type):
        if type == 'csv':
            df = pd.read_csv(path)
        
        return df

    def transform(self, path, type):
        df = self.extract(path, type)
        df['col4'] = df['col1'] + df['col3']
        return df

    def load(self, path, type):
        df = self.transform(path, type)
        df.to_csv('files/csv2.csv', index=False)
        print(f'File: csv2.csv has been created')

    def run(self, path, type):
        self.load(path, type)

etl = SimpleETL()
etl.run('files/csv1.csv', 'csv')