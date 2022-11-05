import random
import time

print("Это 6 случайных цифр из диапазона  от 1 до 52:\nНажмите 'Enter' для старта")
input()
start_list = list(range(1, 53))

num1 = random.choice(start_list)
start_list.remove(num1)
num2 = random.choice(start_list)
start_list.remove(num2)
num3 = random.choice(start_list)
start_list.remove(num3)
num4 = random.choice(start_list)
start_list.remove(num4)
num5 = random.choice(start_list)
start_list.remove(num5)
num6 = random.choice(start_list)
start_list.remove(num6)

list_not_sort = [num1, num2, num3, num4, num5, num6]
for i in range(len(list_not_sort)):
    print(list_not_sort[i], end="  ")
    time.sleep(0.5)
print("\nНажмите 'Enter' для сортировки по возрастанию!")
input()

list_sort = sorted(list_not_sort)
for i in range(len(list_sort)):
    print(list_sort[i], end="  ")
    time.sleep(0.5)
print("\nВот Ваши  цифр!")
print("Нажмите 'Enter'  чтобы закончить")
input()
