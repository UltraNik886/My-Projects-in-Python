name = input("Как зовут вышего персонажа? ")
age = int(input("Сколько лет вашему персонажу? "))
classs = input("Выберете класс (воин/маг/вор) ").lower()

if age >= 10:
    print(f"Привет {name},")

    if classs == "воин":
        print("Ты силён и отважен!")
    elif classs == "маг":
        print("Ты мудр и могущественен!")
    elif classs == "вор":
        print("Ты ловок и скрытен!")
    else:
        print("НЕТ ТАКОГО КЛАССА!")

else:
    print("Ты слишком мал для приключений!")

input()