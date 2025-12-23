from connectors.csv_loader import CSVLoader

class SimpleEtl():
    def __init__(self, type: str, **kwargs):
        self._initialized_attrs = set()

        self.type = type
        self.loaders = {
            'csv':{
                'class': CSVLoader,
                'required_params': ['path'],
                'optional_params': {'delimiter': ',', 'encoding': 'utf-8'}
            }
        }

        self.all_params = self.loaders[self.type]['optional_params'] | kwargs

        for key, value in kwargs.items():
            setattr(self, key, value)
            self._initialized_attrs.add(key)


    def check_all_params(self):
        required_params = self.loaders[self.type]['required_params']
        return all(elem in self._initialized_attrs for elem in required_params)

    def run(self):
        if not self.check_all_params():
            required_params = self.loaders[self.type]['required_params']
            raise ValueError(f"Not all required attributes are listed. \nAll required attributes {required_params}")

        # try:
        #     loader_class = self.loaders[self.type]
        # except KeyError:
        #     # Покажи пользователю, какие типы доступны
        #     available = list(self.loaders.keys())
        #     raise ValueError(f"Unsupported type '{self.type}'. Available: {available}")
        # except TypeError:
        #     required_params = loader_class['required_params']
        #     raise ValueError(f"Need required params: {required_params}")


# Тест 1: Конфликт имен
etl = SimpleEtl('csv', type='json', loaders={}, _initialized_attrs=set())
# Что будет с self.type? А с self.loaders?

# Тест 2: Лишние параметры в CSVLoader
# loader = CSVLoader(path='test.csv', unknown_param='value')
# Будет ли работать? Нужно ли это?

# Тест 3: Отсутствие optional_params в атрибутах
# etl = SimpleEtl('csv', path='test.csv')
# Есть ли у etl атрибут 'encoding' со значением 'utf-8'?

# etl = SimpleEtl('csv', path='files/csv1.csv')
# etl.run()