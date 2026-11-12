
def calculator():
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))
    print("Сума:", a + b)


if __name__ == "__main__":
    print("MyTools v1.0")
    calculator()

def calculator():
    print("=== Калькулятор ===")

    a = float(input("Перше число: "))
    b = float(input("Друге число: "))

    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = input("Вибери операцію (1-4): ")

    if choice == "1":
        print("Результат:", a + b)
    elif choice == "2":
        print("Результат:", a - b)
    elif choice == "3":
        print("Результат:", a * b)
    elif choice == "4":
        if b == 0:
            print("Помилка: ділення на нуль!")
        else:
            print("Результат:", a / b)
    else:
        print("Невідома операція")


if __name__ == "__main__":
    calculator()
