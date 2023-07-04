name = "ШуБадубадуба"

a = name.encode("ko18-r")
b = name.isprintable()

print(name)
print(a)
print(b)


# LookupError: unknown encoding: ko18-r
# Это нельзя напечатать
