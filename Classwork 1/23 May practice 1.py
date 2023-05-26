user_input = input("Enter your salary: ")
salary = int(user_input)

user_input = input("Credit payment per month is: ")
credit = int(user_input)

user_input = input("Utility debt is: ")
utility = int(user_input)

left = salary - (credit + utility)
print("Осталось", left, "денег")
