name = ".-.ШуБадубадуба  \n"

a = name.find("аду", 0, 2)
a = name.index("дуб", 0, 10)
a = name.rfind("дуб")

#name = "Straße"
a = name.lower()
a = name.casefold()

a = name.replace("дуб", "берёза")

a = name.rjust(30, "-")
a = name.ljust(30, "-")
a = name.zfill(60)
a = name.center(30, "-")

a = name.split("дуб")
a = name.partition("дуб")

a = name.strip()
a = name.rstrip()
a = name.lstrip(".-")

name = "белая Берёза Под Моим окном"

a = name.upper()
a = name.lower()
a = name.capitalize()
a = name.title()

a = name.isupper()
a = name.islower()
a = name.istitle()

#name = "2435abcdefg&"

a = name.isdigit()
a = name.isdecimal()
a = name.isalpha()
a = name.isalnum()

#name = name.encode('koi8-r')
#print(name)

a = name.isprintable()

a = list(name)
a.reverse()
a = "".join(a)

print(a)


