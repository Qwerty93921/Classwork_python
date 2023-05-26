user_hours = input("Который час? ")
user_minutes = input("Сколько минут? ")
user_seconds = input("Сколько секунд? ")
seconds_total = 24 * 3600

try:
    hours = int(user_hours)
    minutes = int(user_minutes)
    seconds = int(user_seconds)

except ValueError:
    message = "Вы ввели не числа"

else:
    seconds_passed = hours * 3600 + minutes * 60 + seconds
    seconds_left = seconds_total - seconds_passed
    message = "Осталось %s секунд" % seconds_left

print(message)



# seconds_in_hours = user_hours * 3600
# seconds_in_minutes = user_minutes * 60
# seconds_in_seconds = user_seconds
