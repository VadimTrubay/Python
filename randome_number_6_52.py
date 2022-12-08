import random
import time

print('Это 6 случайных шаров из барабана  от 1 до 52: \n' + \
      '==============================================')
start_list = list(range(1, 53))
new_list = []
time.sleep(1)
for i in range(1, 7):
    num = random.choice(start_list)
    new_list.append(num)
    print(f'Шар номер {i}>: {num}')
    time.sleep(1)
    start_list.remove(num)
time.sleep(2)
print('======================\n' + \
      'в порядке выпадения')
print(', '.join(map(str, new_list)))
time.sleep(2)
print('======================\n' + \
      'после сортировки min>max')
list_sort = sorted(new_list)
print(*list_sort, sep=', ')
time.sleep(2)
print('======================\n' + \
      'программа завершена!')
input()
