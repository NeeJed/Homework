a = int(input("Введите трёхзначное число: "))
result = (a % 100) * 10 + int(a / 100)
str(result)
print("Результат: ", result)
