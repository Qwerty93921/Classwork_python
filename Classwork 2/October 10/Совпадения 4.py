import re

pattern = r"\w[\w\.-_]+@\w[\w\.-_]+\.\w{2,3}"

text = """
Emain addresses: .john.doe@example.www,
jane.smith@example.co.uk
"""

matches = re.findall(pattern, text)
print("Найденные адреса: ", matches)

# Найденные адреса:  ['jane.smith@example.co.uk']
