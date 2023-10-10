import re

pattern = r",\s*"
text = """June 24, 
August 9, \tDec 12"""

result = re.split(pattern, text)
print(result)
# ['June 24', 'August 9', 'Dec 12']

pattern = r"[A-Za-z]+ [0-9]{2}"
# {2} - 2 любых цифры значит
result_text = re.sub(pattern, "Gleb", text)

print(result_text)
# ['June 24', 'August 9', 'Dec 12']
# Gleb, 
# August 9,       Gleb
