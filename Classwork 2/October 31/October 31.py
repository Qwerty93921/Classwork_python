import random
import sys

class Table():
    def __init__(self, size):
        self.size = size
        self.table = []
        for r in range(size):
            self.table.append([])
            for c in range(size):
                self.table[r].append(random.randint(1, 10))

    def __repr__(self):
        s = ""
        for r in self.table:
            s += str(r) + "\n"            
        return s[:-1]

route = list(map(int, sys.argv[1:]))
print("Маршрут: ", route)
size = max(route) + 1
houses = Table(size)
print("Дома: \n",houses, sep="")

result = 0

for i in range(len(route) - 1):
    row = route[i]
    col = route[i + 1]
    result += houses.table[row][col]

print(f"Вам потребуется{result} минут")


# text = str(houses)
# print(text)

# __repr__ переводит в СТРОКУ экземпляр класса
