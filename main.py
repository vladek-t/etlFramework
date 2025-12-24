from connectors.csv_loader import CSVLoader

class SimpleEtl():
    def __init__(self, type: str, **kwargs):
        self.type = type
        self.loaders = {
            'csv':{
                'class': CSVLoader,
                'required_params': ['path'],
                'optional_params': {'delimiter': ',', 'encoding': 'utf-8'}
            }
        }

        required_params = self.loaders[self.type]['required_params']
        optional_params = self.loaders[self.type]['optional_params'].keys()
        self.allowed_params = set(required_params) | set(optional_params)

        self.all_params = kwargs | self.loaders[self.type]['optional_params']

        for key, value in kwargs.items():
            setattr(self, key, value)


    def check_all_params(self):
        check = list(set(self.all_params) ^ set(self.allowed_params))
        return check

    def run(self):
        check_params = self.check_all_params()
        if check_params:
            raise ValueError(f'''
Not all required arguments are filled in or there are extra ones
List of errors: {check_params}
Required and optional params: {self.allowed_params}''')
        else:
            print('Все ок')

        # if not self.check_all_params():
        #     required_params = self.loaders[self.type]['required_params']
        #     raise ValueError(f"Not all required attributes are listed. \nAll required attributes {required_params}")

        # try:
        #     loader_class = self.loaders[self.type]
        # except KeyError:
        #     # Покажи пользователю, какие типы доступны
        #     available = list(self.loaders.keys())
        #     raise ValueError(f"Unsupported type '{self.type}'. Available: {available}")
        # except TypeError:
        #     required_params = loader_class['required_params']
        #     raise ValueError(f"Need required params: {required_params}")



# Случай 1: Все правильно
# etl = SimpleEtl('csv', path='test.csv', delimiter=';')

# Случай 2: Не хватает обязательного
# etl = SimpleEtl('csv', delimiter=';')

# Случай 3: Лишний параметр
# etl = SimpleEtl('csv', path='test.csv', unknown='value')

# Случай 4: Перезапись атрибута
# etl = SimpleEtl('csv', path='test.csv', type='json')

# etl.run()