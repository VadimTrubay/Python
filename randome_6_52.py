import random
import time

print("Это 6 случайных цифр из диапазона  от 1 до 52:\n* нажмите 'Enter' для старта")
input()
start_list = list(range(1, 53))

num1 = random.choice(start_list)
print(num1, end="  ")
start_list.remove(num1)
time.sleep(1)

num2 = random.choice(start_list)
print(num2, end="  ")
start_list.remove(num2)
time.sleep(1)

num3 = random.choice(start_list)
print(num3, end="  ")
start_list.remove(num3)
time.sleep(1)

num4 = random.choice(start_list)
print(num4, end="  ")
start_list.remove(num4)
time.sleep(1)

num5 = random.choice(start_list)
print(num5, end="  ")
start_list.remove(num5)
time.sleep(1)

num6 = random.choice(start_list)
print(num6, end="  ")
start_list.remove(num6)
time.sleep(1)

print(" - нажмите 'Enter' для сортировки по возрастанию!")
input()
list_sort = sorted([num1, num2, num3, num4, num5, num6])
print(list_sort[0], end="  ")
time.sleep(1)
print(list_sort[1], end="  ")
time.sleep(1)
print(list_sort[2], end="  ")
time.sleep(1)
print(list_sort[3], end="  ")
time.sleep(1)
print(list_sort[4], end="  ")
time.sleep(1)
print(list_sort[5], end="  ")
time.sleep(1)

print(" - нажмите 'Enter' для выхода!")
input()
