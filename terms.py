import random

a = random.randint(1, 5)
b = random.randint(1, 5)
print(f'a = {a}, b = {b}')

if b > a:
    print("b больше чем a")
elif a == b:
    print("a равно b ")
else:
    print("a больше чем b")
    print()

x = random.randint(1, 30)
print(f'x = {x}')

if x > 20:
    print("x больше 20")
elif 10 <= x <= 20:
    print("x больше 10, но не больше 20")
else:
    print("x меньше 10")
