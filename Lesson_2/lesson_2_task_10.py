x = int(input("Введите первоначальную сумму вклада: "))
y = int(input("На сколько лет открывается вклад: "))
def bank(x, y):
    for time in range(y):
        x = x * 1.1
    print(round(x, 2))

bank(x, y)