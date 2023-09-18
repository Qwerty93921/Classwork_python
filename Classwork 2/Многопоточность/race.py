import threading

my_lock = threading.Lock()
# Блокировка

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def my_func():
    global numbers
    for j in range(1000):
        # my_lock.acquire() # Блокировка
        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                numbers[i] += numbers[i] - numbers[i - 1] + 1

            else:
                numbers[i] += numbers[i + 1] - numbers[i]

thread_1 = threading.Thread(target=my_func)
thread_2 = threading.Thread(target=my_func)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(numbers)

# [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# -------------------------------------------------------------------------------------------

# https://metanit.com/python/tutorial/2.18.php - lambda

# https://metanit.com/python/tutorial/6.1.php - random, randint, randrange

# randint(a, b) - от A до B числа(включительно)
