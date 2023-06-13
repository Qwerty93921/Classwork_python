def print_weekday(day = 1):
    if day == 1:
        dayname = "Понедельник"
    elif day == 2:
        dayname = "Вторник"
    elif day == 3:
        dayname = "Среда"
    elif day == 4:
        dayname = "Четверг"
    elif day == 5:
        dayname = "Пятница"
    elif day == 6:
        dayname = "Суббота"
    elif day == 7:
        dayname = "Воскресенье"
    print("День недели -", dayname)

    answer = input("Хотите узнать следующий день? ")
    if answer == "да" or answer == "yes":
        day = day + 1
        if day > 7:
            day = 1
        print_weekday(day)

print_weekday()
