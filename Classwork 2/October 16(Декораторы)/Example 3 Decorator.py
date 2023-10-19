def debug(prefix="DEBUG: "):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(prefix + func.__name__)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@debug(prefix="INFO: ")

def say_hello():
    print("Привет")

say_hello()
