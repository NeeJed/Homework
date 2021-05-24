a = int(input("Введите трёхзначное число: "))

def replace(a):
    if type(a) not in [int]:
        raise TypeError("Число должно быть целым")
    if 100 <= a <= 999:
        result = (a % 100) * 10 + int(a / 100)
        str(result)
        print("Результат: ", result)
    else: raise ValueError("Число должно быть трёхзначным")

replace(a)
