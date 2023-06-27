# my_list = [1, 5, 8, 1, 5, 8, 87, 5, 2, 3, 1, 60, 22, 45]
my_list = [6, 65, 50, 52, 54, 54, 54, 0]
          #0 #1 #2 #3 #4 #5 #6

max_length = 0
length = 1

for i in range(len(my_list)-1):
    if my_list[i + 1] >= my_list[i]:
        length += 1
    elif length > max_length:
        max_length = 0
        max_length += length
        length = 1 
    else:
        length = 1
        

print(max_length)

# Числа на увеличение создают список