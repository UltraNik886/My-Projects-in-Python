print("Калькулятор")

while True:
    a = float(input("Введите первое число: "))
    d = input("Выберите действие (+, -, *, /.): ")
    b = float(input("Введите второе число: "))

    if d == "+":
        print(f"{a} + {b} = {a + b}")
    elif d == "-":
        print(f"{a} - {b} = {a - b}")
    elif d == "*":
        print(f"{a} * {b} = {a * b}")
    elif d == "/":
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("---ДЕЛЕНИЕ НА 0 НЕ ВОЗМОЖНО---")
    else:
        print("---ОШИБКА---")

    cont = input("Хотите продолжить? (да/нет)").strip().lower()
    if cont != "да":
        print("Пока!")
        break