x = int(input("Введите число в диапазоне 1 - 999: "))

def rangeNumbers(x):
    if type(x) not in [int]:
        raise TypeError("Число должно быть целым")
    if (x > 999 or x < 1):
        print("невходящее в диапазон ")
        raise ValueError("Число не входит в диапазон")
    else:
        if (x % 2) == 0:
            print("четное ")
        else:
            print("нечётное ")
        if (x <= 999 and x > 99):
            print("трёхзначное ")
        elif (x <= 99 and x > 9):
            print("двухзначное ")
        elif (x <= 9):
            print("однозначное ")
    print("число")

rangeNumbers(x)
