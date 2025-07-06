name = input("Как вас зовут? ")
age = int(input("Сколько вам лет? "))

if age < 12:
    print(f"Извини {name} тебе еще рано...")
elif 12 <= age < 18:
    print(f"Хорошо {name} иди на фильм, но только с родителями.")
else:
    print(f"Отлично, {name}, иди на фильм!")

input()