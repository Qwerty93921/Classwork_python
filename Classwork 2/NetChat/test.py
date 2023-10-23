import hashlib

username = "Vitaliy"
passw = "1235"

# hash = hashlib.md5(passw.encode('utf-8'))

# md5 - тип шифра

# hash = hashlib.md5()
# hash = hashlib.sha1()
hash = hashlib.sha512()


hash.update(username.encode('utf-8'))
hash.update(passw.encode('utf-8'))


hash_string = hash.hexdigest()
print(hash_string)
