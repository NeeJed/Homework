a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))
s = 0

while (a - c >= 0):
    a = a - c
    btemp = b
    while (btemp - c >= 0):
        btemp = btemp - c
        s = s + 1
print(s)
