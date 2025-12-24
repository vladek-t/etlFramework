from connectors.csv_loader import CSVLoader

class SimpleEtl():
    def __init__(self, type: str, **kwargs):
        RESERVED_ATTRS = {'type', 'loaders', 'loader_all_params', 'all_params'}
        self.type = type

        self.loaders = {
            'csv':{
                'class': CSVLoader,
                'required_params': ['source_path', 'target_path'],
                'optional_params': {'delimiter': ',', 'encoding': 'utf-8'}
            }
        }

        # Проверка переданного типа
        if self.type not in self.loaders.keys():
            raise ValueError(f"Invalid source type.\nAvailable source types: {self.loaders.keys()}")

        required_params = self.loaders[self.type]['required_params']
        optional_params = self.loaders[self.type]['optional_params']
        allowed_params = set(required_params) | set(optional_params.keys())

        # Обязательные параметры
        missing_required = [
            param for param in required_params 
                if param not in kwargs
        ]

        # Проверка лишних параметров
        extra_params = [
            param for param in kwargs.keys()
                if param not in allowed_params
        ]

        self.all_params = {}

        if missing_required:
            raise ValueError(f"Required attributes are not specified.\nRequired attributes that are not specified: {missing_required}")
        elif extra_params:
            raise ValueError(f"Extra attributes specified.\nExtra attributes: {extra_params}")

        for key, value in kwargs.items():
            if key in RESERVED_ATTRS:
                raise AttributeError(f"Cannot use reserved name '{key}' as parameter")
            setattr(self, key, value)
            self.all_params[key] = value

        self.all_params = self.all_params | optional_params


    def run(self):
        loader_class = self.loaders[self.type]['class'](**self.all_params)
        loader_class.run()


etl = SimpleEtl('csv', source_path='files/csv1.csv', target_path='files/csv2.csv')
etl.run()