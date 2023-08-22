def more_than(a, key=None): # a = список
    if key is None:
        key = lambda x: x
    else:
        key(a[i]) > key(a[i + 1])


    # if key is not None:
    #     key(a[i]) > key(a[i + 1])
