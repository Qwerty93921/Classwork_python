show_mul_table(n, i = 2):
    if i >= 10:
        return
    print(n * i)
    show_mul_table(n, i + 1)

show_all_table(n = 2):
    if n >= 10:
        return
    show_mul_table(n)
    show_all_table(n + 1)
    print()
