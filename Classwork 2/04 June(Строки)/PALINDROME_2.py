my_file = open("palindrome.txt", encoding="utf-8")

text = my_file.read()
my_file.close()

text = filter(lambda x: x == x[::-1], text.split())
text = ", ".join(text)
print(text)

# казак, и, мем, шалаш, тут, казак, око, и, А