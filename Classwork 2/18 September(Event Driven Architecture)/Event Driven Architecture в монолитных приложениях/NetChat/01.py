import os
from functools import lru_cache

@lru_cache
def readFile(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

print(readFile('input.txt'))
os.remove("input.txt")
print(readFile('input.txt'))
