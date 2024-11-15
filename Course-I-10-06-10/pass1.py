import random
import string

password_length = 12

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(characters, k=password_length))

print(f'Password: {password}')
