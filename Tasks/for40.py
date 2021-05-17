a = int(input("Введите A: "))
b = int(input("Введите B: "))
res = b - a
temp = a
x = 0
while x <= res:
    y = 0
    while y <= x:
        print(temp)
        y = y + 1
    x = x + 1
    temp = temp + 1
    
