def range_guard(func):
    def wrapper(*args, **kwargs):
        # Перевіряємо всі позиційні аргументи
        for arg in args:
            if not (isinstance(arg, (int, float)) and 0 <= arg <= 100):
                raise ValueError(f"Аргумент {arg} не у діапазоні 0..100")
        
        # Перевіряємо іменовані аргументи
        for name, value in kwargs.items():
            if not (isinstance(value, (int, float)) and 0 <= value <= 100):
                raise ValueError(f"Аргумент {name}={value} не у діапазоні 0..100")

        return func(*args, **kwargs)
    return wrapper
