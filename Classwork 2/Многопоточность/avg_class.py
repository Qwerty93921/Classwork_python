import threading
numbers = tuple(range(50))
result = 0
lock = threading.Lock()

def average(numb):
    sum = 0
    for x in numb:
        sum += x
    global result
    # global - значит это ГЛОБАЛЬНАЯ переменная которую ВИДНО ВЕЗДЕ, ВНЕ ФУНКЦИИ и т.д. 

    # lock.acquire()
    # Блокировка может быть для не повреждения данных
    result += sum/len(numb)
    # lock.release()

thread_1 = threading.Thread(target = average, args = ( (numbers[:10]), ) )
thread_2 = threading.Thread(target = average, args = ( (numbers[10:20]), ) )
thread_3 = threading.Thread(target = average, args = ( (numbers[20:30]), ) )
thread_4 = threading.Thread(target = average, args = ( (numbers[30:40]), ) )
thread_5 = threading.Thread(target = average, args = ( (numbers[40:50]), ) )

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()

result = result / 5

print(result)

# 24.5
