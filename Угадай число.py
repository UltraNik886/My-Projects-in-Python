import random

c1 = int(random.randint(1, 10))
altem = 0

p1 = int(input("Я загадал число от 1 до 10, угадай! "))

if p1 > 10:
    print("Это число слишком большое!")
    exit()
while p1 != c1:
    altem += 1
    p1 = int(input("Ты не угадал, попробуй еще раз!"))
    if p1 > 10:
        print("Это число слишком большое!")
        exit()

print(f"Ты угадал с {altem} попытки!")
input()