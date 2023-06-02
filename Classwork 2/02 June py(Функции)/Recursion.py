def recur(num):
    if num < 0:
        return
    print(num)
    recur(num-1)
    print(num)

recur(4)
