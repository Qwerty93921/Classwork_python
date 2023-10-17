from random import randint

class Matrix():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        big_list = []

        for gorizontal_elem in range(len(rows)):
            big_list.append(gorizontal_elem)
            print(gorizontal_elem)

        for vertical_elem in range(len(cols)):
                big_list.append(vertical_elem)
                print(vertical_elem)

    def set(sds, row, cells):
        pass

    def __next__(self):
        pass

my_matrix = Matrix(3, 3)

# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]
# ]
