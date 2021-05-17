check = True
N = int(input("Введите число: "))
k = 1
while (k < N - 1):
    k = k + 1
    if (N % k == 0): check = False
print(check)
