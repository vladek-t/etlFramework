from connectors.csv_loader import CSVLoader


class SimpleEtl():
    def __init__(self, type: str, **kwargs):
        self._initialized_attrs = set()

        self.type = type
        self.loaders = {
            'csv':{
                'class': CSVLoader,
                'required_params': ['path', 'main'],
                'optional_params': {'delimiter': ',', 'encoding': 'utf-8'}
            }
        }

        for key, value in kwargs.items():
            setattr(self, key, value)
            self._initialized_attrs.add(key)


    def check_all_params(self):
        required_params = self.loaders[self.type]['required_params']
        optional_params = self.loaders[self.type]['optional_params']

        # print(all(elem in self._initialized_attrs for elem in required_params))
        return all(elem in self._initialized_attrs for elem in required_params)

    def run(self):
        if not self.check_all_params():
            raise ValueError(f"Need required params")

        # try:
        #     loader_class = self.loaders[self.type]
        # except KeyError:
        #     # Покажи пользователю, какие типы доступны
        #     available = list(self.loaders.keys())
        #     raise ValueError(f"Unsupported type '{self.type}'. Available: {available}")
        # except TypeError:
        #     required_params = loader_class['required_params']
        #     raise ValueError(f"Need required params: {required_params}")


etl = SimpleEtl('csv', path='files/csv1.csv')
# etl.run()
etl.run()