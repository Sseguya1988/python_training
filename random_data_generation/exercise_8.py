# Exercise 8: Generate random secure token of 64 bytes and random URL
import secrets
import random
import string
# generate a secure token of 64 bytes
secure_token = secrets.token_hex(64)  # 32 bytes yields 64 characters
# generate a random URL with a random path in lowercase letters
url_characters = string.ascii_letters + string.digits + "-_"
url = ''.join(secrets.choice(url_characters) for _ in range(64))
# url = "https://example.com/" + "".join(random.choice(string.ascii_lowercase) for _ in range(10))
print(f"The secure token is given by {secure_token}")
print(f"The secure url is {url}")
# print(secrets.token_bytes(64))

