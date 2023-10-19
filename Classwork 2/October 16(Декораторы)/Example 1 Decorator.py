def my_decorator(func):
    def wrapper():
        print("Что то происходит перед выхова функции")
        func()
        print("Что то происходит после выхова функции")
    return wrapper

@my_decorator
# Вызов всего что ниже функции my_decorator

def say_hello():
    print("Привет")

decorated_say_hello = my_decorator(say_hello)
decorated_say_hello()
