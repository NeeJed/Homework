N = int(input("Введите число: "))

def check_true(N):
    check = True
    k = 1
    while (k < N - 1):
        k = k + 1
        if (N % k == 0): check = False
    print(check)

check_true(N)
