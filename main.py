import loaders
from loaders.registry_loaders import get_loader

class SimpleEtl():
    def __init__(self, type: str, **kwargs):
        # Зарезервированные атрибуты в классе
        RESERVED_ATTRS = {'type', 'all_params', 'loader_info'}

        # Получение информации о параметрах загрузчика
        self.loader_info = get_loader(type)
        if not self.loader_info:
            raise ValueError(f"No loader for type: {type}")
        
        # Списки обязательных и не обязательных параметров для загрузчика
        required_params = self.loader_info['required_params']
        optional_params = self.loader_info['optional_params']
        allowed_params = set(required_params) | set(optional_params.keys())

        # Проверка наличия всех обязательных параметров
        missing_required = [
            param for param in required_params
                if param not in kwargs
        ]
        if missing_required:
            raise ValueError(f"Required attributes are not specified.\nRequired attributes that are not specified: {missing_required}")

        # Проверка лишних параметров
        extra_params = [
            param for param in kwargs.keys()
                if param not in allowed_params
        ]
        if extra_params:
            raise ValueError(f"Extra attributes specified.\nExtra attributes: {extra_params}")

        # Словарь, хранящий все параметры для передачи загрузчику
        self.all_params = {}

        for key, value in kwargs.items():
            if key in RESERVED_ATTRS:
                raise AttributeError(f"Cannot use reserved name '{key}' as parameter")
            self.all_params[key] = value

        self.all_params = self.all_params | optional_params

    def run(self):
        try:
            loader_class = self.loader_info['class']
            loader_instance = loader_class(**self.all_params)
            loader_instance.run()
        except FileNotFoundError as e:
            raise ValueError(f"File not found: {e.filename}") from e
        except Exception as e:
            raise RuntimeError(
                f"Failed to run {self.type} loader. "
                f"Check your parameters: {self.all_params}. "
                f"Error: {e}"
            ) from e


etl = SimpleEtl(type='csv', source_path='files/csv3.csv', target_path='files/csv2.csv')
etl.run()