import random
import time

print("Это 6 случайных цифр из диапазона  от 1 до 52: ")
print('======================')
start_list = list(range(1, 53))
new_list = []
for i in range(1, 7):
    num = random.choice(start_list)
    new_list.append(num)
    print(num)
    time.sleep(1)
    start_list.remove(num)
time.sleep(1)
print('в порядке выпадения')
print(', '.join(map(str, new_list)))
time.sleep(2)
print('======================')
print('после сортировки по возрастанию')
# print(str(new_list).strip('[]'))
list_sort = sorted(new_list)
print(*list_sort, sep=', ')