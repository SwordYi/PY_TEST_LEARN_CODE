import hashlib

md5 = hashlib.md5(b"123456")
password_md5 = md5.hexdigest()
print(md5)
print(password_md5)

sha512 = hashlib.sha512(b"123456")
password_sha512 = sha512.hexdigest()
print(password_sha512)
