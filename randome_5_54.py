import random
import time

lst1 = list(range(1, 53))
num1 = random.choice(lst1)
lst1.remove(num1)

lst2 = lst1
num2 = random.choice(lst2)
lst2.remove(num2)

lst3 = lst2
num3 = random.choice(lst3)
lst3.remove(num3)

lst4 = lst3
num4 = random.choice(lst4)
lst4.remove(num4)

lst5 = lst4
num5 = random.choice(lst5)
lst5.remove(num5)

lst6 = lst5
num6 = random.choice(lst6)
lst6.remove(num6)

listen = [num1, num2, num3, num4, num5, num6]

list_sort = sorted([num1, num2, num3, num4, num5, num6])

print(lst6)
time.sleep(2)
print(listen)
time.sleep(2)
print(list_sort)
input()







