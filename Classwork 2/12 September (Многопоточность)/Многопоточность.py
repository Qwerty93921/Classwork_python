import threading

def worker_function():
    print("Работник выполняет задачу")

thread = threading.Thread(target=worker_function)
# Создание потока

thread.start()
# Запуск потока

# Глобальная блокировка интерпретатора
# GIL - предотвращает одновременное выполнение одного и того же кода в нескольких потоках. Это значит что в многопоточной программе на Python одновременно выполняется только
# 1 поток, даже если у вас несколько ядер процессора

# GIL был введен для обеспечения простоты реализации и избежания сложностей, связанных с многозадачностью на уровне интерпретатора

# Блокировка и МЬЮТЕКС похожи но работают по разному
# Блокировка - блокирует все остальное пока выполняется 1 действие, мьютекс - разрешает делать остальные процессы, но чтобы не трогали тот который сейчас идет
