def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
# Вызов функции 3 раза

def say_hello():
    print("Привет")

say_hello()
