
def calculator():
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))

    print("Додавання:", a + b)
    print("Віднімання:", a - b)
    print("Множення:", a * b)

    if b != 0:
        print("Ділення:", a / b)
    else:
        print("Ділення на нуль неможливе!")


if __name__ == "__main__":
    print("MyTools v2.0")
    calculator()
