x = int(input("Введите число в диапазоне 1 - 999: "))
if (x > 999):
    print("невходящее в диапазон ")
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
