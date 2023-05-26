# user_GB = int(input("Введите объем flash в ГБ: "))
# file_MB = int(input("Введите размер файла в MB: "))
# GB_in_MB = user_GB * 1024

# try:
#     GB = int(user_GB)
#     MB = int(file_MB)

# except ValueError:
#     print("Вы ввели неверные значения")

# else:
#     MB_full = user_GB * 1024
#     MB_left = MB_full - file_MB
#     amount_of_file_copies = MB_left // file_MB

# print("Столько копий файла будет: ", amount_of_file_copies)


user_GB = int(input("Введите объем flash в ГБ: "))
file_MB = int(input("Введите размер файла в MB: "))
GB_in_MB = user_GB * 1024

try:
    MB_full = user_GB * 1024
    MB_left = MB_full - file_MB
    amount_of_file_copies = MB_left // file_MB

except ValueError:
    print("Вы ввели неверные значения")


print("Столько копий файла будет: ", amount_of_file_copies)
