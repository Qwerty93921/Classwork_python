import time


def recur(num):
    time.sleep(1)
    if num < 0:
        return
    print(num)
    recur(num-1)
    print(num)


recur(4)
