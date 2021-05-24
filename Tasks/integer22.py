TimeS = int(input("Введите количество секунд: "))

def minutes(TimeS):
    if type(TimeS) not in [int]:
        raise TypeError("Число должно быть целым")
    if TimeS > 0:
        T = TimeS % (60*60)
        print("Количество секунд с последнего часа: ", T)
    else: raise ValueError("Число секунд должно быть положительным")

minutes(TimeS)
