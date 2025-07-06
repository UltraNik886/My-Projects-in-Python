name = input("Ваше имя? ")
age = int(input("Ваш возраст? "))

if 16 <= age <= 21 and name[0].upper() == "А":
    print("Добро пожаловать в клуб!")
else:
    print("Доступ к клубу закрыт")

input()