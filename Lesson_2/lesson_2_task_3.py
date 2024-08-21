import math


side = float(input("Сторона квадрата: "))
def square(side):
    return math.ceil(side*side)
result = square(side)
print(result)