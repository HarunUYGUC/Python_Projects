
""" I created a mixed password with 2 lowercase letters, 2 uppercase letters, 2 numbers and 2 symbols. """

import random
import string

all_keys = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
password = ""

for i in all_keys:
    for j in range(2):
        password += random.choice(i)

password = list(password)
random.shuffle(password)

last_password = ""

for key in password:
    last_password += key

print(last_password)
