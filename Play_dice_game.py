import random
import time

PlayerOne = "Вася"
PlayerTwo = "Петя"

VasyaScore = 0
PetyaScore = 0

# У каждого кубика шесть возможных значений
diceOne = [1, 2, 3, 4, 5, 6]
diceTwo = [1, 2, 3, 4, 5, 6]


def playDiceGame():
    """Оба участника, Вася и Петя, бросают кубик, используя метод shuffle"""

    for i in range(5):
        # оба кубика встряхиваются 5 раз
        random.shuffle(diceOne)
        random.shuffle(diceTwo)
    firstNumber = random.choice(diceOne)  # использование метода choice для выбора случайного значения
    SecondNumber = random.choice(diceTwo)
    return firstNumber + SecondNumber

print("Игра в кости использует модуль random\n")

# Давайте сыграем в кости три раза
#for i in range(3):
    # определим, кто будет бросать кости первым
VasyaTossNumber = random.randint(1, 100)  # генерация случайного числа от 1 до 100, включая 100
PetyaTossNumber = random.randrange(1, 101, 1)  # генерация случайного числа от 1 до 100, не включая 101

if (VasyaTossNumber > PetyaTossNumber):
    print("Вася выиграл жеребьевку.")
    time.sleep(1)
    VasyaScore = playDiceGame()
    PetyaScore = playDiceGame()
else:
    print("Петя выиграл жеребьевку.")
    time.sleep(1)
    VasyaScore = playDiceGame()
    PetyaScore = playDiceGame()

if (VasyaScore > PetyaScore):
    print(f"Финальный счет Пети: {PetyaScore}")
    time.sleep(1)
    print(f"Финальный счет Васи: {VasyaScore}")
    time.sleep(1)
    print("Вася выиграл игру в кости.")
elif (VasyaScore < PetyaScore):
    print(f"Финальный счет Васи: {VasyaScore}")
    time.sleep(1)
    print(f"Финальный счет Пети: {PetyaScore}")
    time.sleep(1)
    print("Петя выиграл игру в кости.")
else:
    print(f"Финальный счет Васи: {VasyaScore}")
    time.sleep(1)
    print(f"Финальный счет Пети: {PetyaScore}")
    time.sleep(1)
    print(f"Победила дружба!")