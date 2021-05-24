a = int(input("Введите число: "))
def check_twosimple(a):
    if type(a) not in [int]:
        raise TypeError("Число должно быть целым")
    print((a > 9) and (a < 100) and (a % 2 == 0))

check_twosimple(a)
