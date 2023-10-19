class MyIterator:
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# raise - выбросить исключение
# except = raise

my_iterator = MyIterator(10)

for item in my_iterator:
    print(item)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
