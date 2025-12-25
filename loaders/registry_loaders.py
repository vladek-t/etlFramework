"""
Регистрация загрузчиков для передачи их параметров в основной файл
"""

_loaders = {}

def register_loaders(name, loader_class, required_params, optional_params):
    _loaders[name] = {
        'class': loader_class,
        'required_params': required_params,
        'optional_params': optional_params
    }

def get_loader(name):
    return _loaders.get(name)