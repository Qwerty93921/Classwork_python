def my_func():
    yield "Hello"
    yield "How are you?"
    yield"Goodbye"
    yield"Yooooo"

# it = my_func()
# next(it)

# yield - остановится после действия ДО yield
# yield как return

# python -i название файла.py
# писать после запуска каждый раз next(it)

for x in my_func():
    print(x)

it = my_func()
result = list(map(lambda x: x.upper(), it))
print(result)

# Hello
# How are you?
# Goodbye
# Yooooo
# ['HELLO', 'HOW ARE YOU?', 'GOODBYE', 'YOOOOO']
