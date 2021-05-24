a = int(input("Введите 1 сторону: "))
b = int(input("Введите 2 сторону: "))
c = int(input("Введите 3 сторону: "))

def triangle_true(a,b,c):
    if (type(a) or type(b) or type(c)) not in [int]:
        raise TypeError("Число должно быть целым")
    print((a == b) or (b == c) or (c == a))

triangle_true(a,b,c)
