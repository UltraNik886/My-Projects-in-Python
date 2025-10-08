import random
import string

length = int(input("Введите длину пароля: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Ваш пароль:", password)