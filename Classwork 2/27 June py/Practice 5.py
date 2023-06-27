def make_groups(num, pairs):
    groups = []
    pairs.sort(key=get_marks, reverse=True)
    group_member = len(pairs) // num
    for i in range(len(pairs)):
        if group_member 
    return groups

def get_marks(whole_group):
    for i in range(len(whole_group)):
        return whole_group[1]



names = ["Артем", "Руслан", "Ансар", "Глеб", "Шолпан", "Латифа", "Даниил", "Саша", "Саня", "Санёк"]
marks = [10, 9, 11, 5, 6, 9, 7, 4, 2, 6]


students = list(zip(names, marks))
print(students)
gr = make_groups(2, students)
print(students)

# zip - соединяет 2 списка в 1
# если 1 список длиннее второго, то оставшееся не добавяется в новый список
# Артем 10, Руслан 9, Ансар 11, Глеб 5 и тд
