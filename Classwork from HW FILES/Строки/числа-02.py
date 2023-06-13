user_in = input("Сколько сейчас часов? ")
hours = int(user_in)

user_in = input("Сколько сейчас минут? ")
minutes = int(user_in)

hours_remain = 23 - hours
minutes_remain = 60 - minutes

print("Осталось", hours_remain,
       "ч", minutes_remain, "мин")

