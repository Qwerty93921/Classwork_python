# https://www.fusd1.org/cms/lib/AZ01001113/Centricity/Domain/1385/harry%20potter%20chapter%201.pdf
# Harry Potter and philosopher's stone text

def read_large_file(file_path):
    with open(file_path, "r", encoding="utf-8") as myFile:
        print(dir(myFile))
        # dir - свойства и методы в виде списка показывает из текста
        for line in myFile:
        # line = '\n'
        # while line != '':
        #     line = myFile.readline()
            yield line

def process_line(line):
    print(line)

for line in read_large_file("big_data.txt"):
    process_line(line)
