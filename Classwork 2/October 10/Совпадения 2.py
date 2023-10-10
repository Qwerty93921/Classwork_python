import re

# ^ - начало строки
# $ - конец строки

pattern = r'(?P<month>[a-z]+) (?P<day>\d+) *$'
text = "June 24, September 20, October 10    "

matched = re.search(pattern, text, re.IGNORECASE)

if matched:
    print("Группа 0", matched.group(0))
    print("Группа 1", matched.group('month'))
    print("Группа 2", matched.group('day'))

# Группа 0 October 10    
# Группа 1 October
# Группа 2 10
