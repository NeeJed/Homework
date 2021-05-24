a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))

def numberOfSquares(a,b,c):
    if (type(a) or type(b) or type(c)) not in [int]:
        raise TypeError("Число должно быть целым")
    if (a < 0 or b < 0 or c < 0):
        raise ValueError("Число должно быть положительным")
    s = 0
    while (a - c >= 0):
        a = a - c
        btemp = b
        while (btemp - c >= 0):
            btemp = btemp - c
            s = s + 1
    print(s)

numberOfSquares(a,b,c)
