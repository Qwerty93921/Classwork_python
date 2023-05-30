user_km = int(input("Введите количество км между городами: "))
user_hours = int(input("За сколько часов вы хотите добраться до города?: "))
needed_speed = user_km / user_hours

print("Вам потребуется данная скорость (км/ч) чтобы добраться до города", needed_speed)