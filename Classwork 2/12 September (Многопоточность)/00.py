import threading
import time

def my_func():
    time.sleep(3) # Задержка 3 секунды
    print("Я проснулся")

my_thread = threading.Thread(target=my_func)
my_thread.start()

print("А это продолжается главный поток")

my_thread.join()
print("Конец")

# python .\00.py
# python .\название файла
