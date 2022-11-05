import random
import time
koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

random.shuffle(koloda)

print('Поиграем в очко?')
score = 0

while True:
    time.sleep(1)
    choice = input('Будете брать карту? y/n: \n')
    if choice == 'y':
        current = koloda.pop()
        print(f'Вам попалась карта достоинством {current}')
        score += current
        if score > 21:
            print('Извините, но вы проиграли')
            break
        elif score == 21:
            print('Поздравляю, вы набрали 21 и выиграли!')
            break
        else:
            print(f'У вас {score} очков.')
    elif choice == 'n':
        print(f'У вас {score} очков и вы закончили игру.')
        break
time.sleep(1)
print('До новых встреч!')
input()
