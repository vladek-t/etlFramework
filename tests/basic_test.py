import os
import sys
# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import SimpleEtl


# Тест 1: CSVLoader работает
etl = SimpleEtl('csv', 
                source_path='files/csv1.csv',
                target_path='files/csv2.csv',
                delimiter=';',  # Переопределяем дефолтный delimiter
                encoding='cp1251')  # Переопределяем дефолтный encoding
etl.run()

# Тест 2: Проверка, что файл создан
assert os.path.exists('files/csv2.csv'), "Output file not created"

# Тест 3: Проверка с дефолтными параметрами
etl2 = SimpleEtl('csv',
                 source_path='files/csv1.csv',
                 target_path='files/csv3.csv')
etl2.run()  # Должен использовать delimiter=',' и encoding='utf-8'