'''from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.GREEN)
print(Back.WHITE)
print(Style.DIM)'''

#дебильный калькулятор
'''import colorsys
import time'''

'''a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
operation = input("что делаем?(+, -, * , /): ")
result = 0
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
print(f"Результат: {result}")'''

# import sys
'''print(sys.version)'''

# это f строка сложения
'''name = "Vad"
weather = "Oblachno"
sum = 11.5
print(f"Привет {name}, сегодня {weather}, а у меня в кармане {sum} $")
weight = input("Введите ваш вес: ")#print(f"Ваш вес {weight} kg")'''

# модуль random генератор рандомных чисел
'''import random
print(random.randint(1, 54))
print(random.randint(1, 53))
print(random.randint(1, 52))
print(random.randint(1, 51))
print(random.randint(1, 50))'''

# угадай число
'''import random
num = random.randint(1, 100.)
while True:
    print("угадай число от 1 до 100: ")
    guesse = input()
    i = int(guesse)
    if i == num:
        print('ты угадал!')
        break
    elif i < num:
        print('загаданое число больше')
    elif i > num:
        print('загаданое число меньше')'''

# перетасовка списка функция shuffle
'''import random
desert = ['морожка1', 'пирожка2', 'творожка3', 'кекс4']
random.shuffle(desert)
print(desert)'''

# Управление оболочкой с помощью модуля sys
'''import  sys
sys.exit()'''

# Ввод данных и объект stdin(стандартный ввод standart input)
'''import sys
print("введите слово: ")
inp = sys.stdin.readline(5)
print(f'вы ввели слово: {inp}')'''

# Вывод данных и объект stdout (стандартный вывод standart out)типа (print)
'''import sys
inn = sys.stdout.write('dgchckmchgjmv')
print(inn)'''

# преобразование к целому
'''import math
x = 13.9
print(math.floor(x))'''

# игра угадай число
'''import random
randomNumber = random.randint(1, 5)
userNumber = int(input("Давай отгадаем число, \nот 1 до 5, попытка номер рас: "))
if userNumber == randomNumber:
    print(f"загаданый номер {randomNumber}, ")
    print("хорошая попытка бро!!!\n")
else:
    print(f"загаданый номер {randomNumber}, ")
    print("ты ошибся Кутузов, давай досвидиния!!!")'''

# метка %s
'''myScore = 5886
message = ("мой счет %s очков")
print(message % myScore)'''

# bodyPart1 = "Коленка"
'''odypart2 = "Большой палец ноги"
print(jokeText % bodyPart1)
print(jokeText % bodypart2)'''

# nums = "что сказало число %s, числу %s? Славный поясок!"
'''print(nums % (0,8))'''

# spaice = ' ' * 25
'''print("%s впереди есть 25 пробелов "% spaice)'''

# print(10 * "слякоть\n")

# списки или массивы
'''produktList = ["молоко", "масло", "сметана", "сливки", "кефир"]
produktList[3] = "оливки"
print(produktList[1:4])'''

# someNumbers = [1, 2, 3]
'''someString = ["one", "two", "three"]'''

# добавление и удаление елементов списка
'''someNumbers.append("4")
someString.append("five")
del someNumbers[0]'''

# список в списке
'''someNumberAndString = [someNumbers, someString]
someNumberAndString = [someNumbers + someString]
myList = [someNumbers, someString, someNumberAndString]
print(myList)'''

# кортежи(неизменные после создания)последовательность фибоначчи
'''fibs = (1, 2, 3)
print(fibs[2])
fibs [2] = 4'''

# словарь(ключ-значение)
'''favoriteSports = {"андрей шевченко": "футбол", "рафаель надаль": "тенис", "михаель шумахер": "гонки"}
print(favoriteSports["рафаель надаль"])
favoriteSports ["андрей шевченко"] = "пиздабол"
print(favoriteSports)
del favoriteSports["михаель шумахер"]
print(favoriteSports)'''

# myFirstName = "vadim"
'''myLastName = "trubay"
myName = "my name %s %s"
print(myName %(myFirstName, myLastName))'''


# условия if else elif
'''age = 39
if age > 40:
    print("Ты старый пердун")
elif age == 40:
    print("ну такое")
else:
    print("да ты ещё могёшь")'''

# пустое значение None
'''myVar = None
if myVar == None:
    print("тут пусто братан")'''

# преобразование строки в число и наоборот
'''age = '10.5'
newAge = int(age)
newAge = str(age)
newAge = float(age)
if newAge == 10.5:
    print("this is 10")'''

'''twinkiers = 666
if twinkiers < 100:
    print("маловато  вася")
elif twinkiers > 500:
    print("многовато вася")'''

'''money = 1222
if money >= 100 and money <= 500:
    print("ok")
elif money >=1000 and money<= 5000:
    print("ok")
else:
    print("not good")'''

# циклы for и while
'''for x in range(0, 3):
    print("good")
print (list(range(1, 10)))'''

'''produktList = ["молоко", "масло", "сметана", "сливки", "кефир"]
for x in produktList:
    print(x)'''

'''hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
         print(j)'''

'''foundCoins = 20
magicCoins = 70
stolenCoins = 3
coins = foundCoins
for week in range(1, 53):
    coins = coins + magicCoins - stolenCoins
    print(f"неделя {week} = {coins} монеты")'''

'''step = 0
tired = False
badweather = False
while step < 50:
    if tired == True:
            break
    elif badweather == True:
            break
    else:
        step = step + 1
        print(step)'''

'''x = 10
y = 20
while x < 50 and y < 100:
    x = x + 8
    y = y + 5
    print(x, y)'''

# for x in range(0, 20):
#     print(f'привет {x}')
#     if x > 9:
#         break

'''x = 0
while x <40:
    x = x + 2
    print(x)'''

# путешествие на луну с весом 85 кг
'''weight = 85
newWeight = weight * 0.165
for day in range (1, 16):
    newWeight = newWeight + 1
    print(f"@год {year} = {newWeight}")'''

# функции твою мать!
'''def testFunc(myName):
    print(f"hello, {myName}")
testFunc("vad")

    print(f"hello, {firstName} {lastName}")
testFunc("vad", "trubay")'''

'''def testFunc(firstName, lastName):
    print(f"hello, {firstName} {lastName}")
firstName = "vad"
lastName = "trubay"
testFunc(firstName, lastName)'''

'''def savings ():
    poscetMoney = 10
    paperRout = 10
    spending = 8
    return poscetMoney * paperRout - spending
print(savings())'''

'''def variableTest():
    firstVariable = 10
   lastVariable = 20
    return firstVariable * lastVariable
print(variableTest())'''

'''def spshb(cans):
    totalCanc = 0
    for week in range(1, 53):
       totalCanc = totalCanc + cans
        print(f"Неделя - {week}, банок: {totalCanc}")
spshb(4)'''

'''import  time
print(time.asctime())
import  sys
def silly_age_joke():
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
         print('ты подросток')
    else:
        print('ты слишком глуп')
#silly_age_joke()'''

'''def moonWeight (weight, plusyear, year):
    return weight * plusyear * year
print(moonWeight(85, 0.25, 5))'''

# import sys
# def moonWeight():
#     print("Введите Ваш земной вес: ")
#     weight = int(sys.stdin.readline())
#     print("Введите ежегодную прибавку веса: ")
#     weightPlus = float(sys.stdin.readline())
#     print("Введите количество лет : ")
#     age = int(sys.stdin.readline())
#     return weight * weightPlus * age
# print(f"Ваш лунный вес составит {moonWeight()}")


# обьекты и класы
'''class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')

class Mammals(Animals):
    def feed_young_with_milk(self):
          print('кормит детенышей молоком')'''

'''class Giraffes(Mammals):
    def lff(self):
        print("левая нога вперед")
    def lfb(self):
        print("левая нога назад")
    def rff(self):
        print("правая нога вперед")
    def rfb(self):
        print("правая нога назад")
    def dance(self):
        self.lff()
        self.lfb()
        self.rff()
        self.rfb()
        self.lfb()
        self.rfb()
        self.rff()
        self.lff()'''

'''   def __init__(self, spots):
        self.giraffe_spots = spots'''

'''   def eat_leaves_from_trees(self):
         print('ест листья')
         def find_food(self):
        self.move()
        print("Я нашел еду!")
        self.eat_food()'''

'''   def eat_leaves_from_trees(self):
        self.eat_food()'''

'''   def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()'''

'''rejinald = Giraffes()
rejinald.eat_leaves_from_trees()
rejinald.dance_a_jig()
rejinald.dance()
harold = Giraffes(20)
harold.move()
harold.find_food()
ozvald = Giraffes(100)
gertrude = Giraffes(150)
print(ozvald.giraffe_spots)
print(gertrude.giraffe_spots)'''


# функция abs(возвращает абсолютное значение (модуль) числа, то есть само число без знака)
'''steps = -3
if abs(steps) > 0:
   print("чувак двигаеться")
else:
    print("чувак стоит")'''

# функция bool(принимает один аргумент и в зависимости от его значения возвращает True или False)
'''year = input('введите год рождения: ')
if not bool (year.rstrip()):
    print('вам нужно ввести день рождения')'''

# функция dir(выдает информацию о любом переданном ей значении)
# функция help(получить краткую справку по любой функции из этого списка)
'''popcorn = "я люблю попкорн"
dir(popcorn)
help(popcorn.split())'''

# функция eval(принимает в качестве аргумента строку и выполняет ее)
'''calc = (input('введите выражение: '))
print(eval(calc))'''

# фунция exec(выполнять)
'''mySmallProgram ="print('бутерброд с колбасой')"
exec(mySmallProgram)'''

# функция float(преобразует строку или число в вещественное число)
'''iint = "12"
print(float(iint))'''

'''iint = "12.23135468"
print(float(iint))'''

'''age = float(yourage)
aass = age - 13
if age > 13:
    print(f"вы на {aass} моложе чем положено ")'''''

# функция  int(преобразование строки или числа в целое число)
'''print(int(1235.3215))
print(int("313"))'''

# функция len (длина объекта)
'''print(len('это тестовая строка'))'''

'''fruit = ['яблоко', 'банан', 'маракуйя', 'папайя']
length = len(fruit)
for x in range(0, length):
    print(f'фрукт с индексом {x}: {fruit[x]}')'''

# функции min и max(минимальное и максимальное значение)
'''numb = [5, 45, 434, 35656, 3435456]
print(max(numb))
print(min(numb))'''

'''string = 'этосторокастрокаСТРОКАя'
print(max(string))
print(min(string))'''

'''guesThisNumber  = 60
pleerGuesssees = [2, 12, 55, 45]
if max(pleerGuesssees) > guesThisNumber:
    print('ты проиграл')
else:
    print('ты выиграл')'''

# функция range(старт стоп интервал)
'''for x in range(0, 9, 2):
    print(x)
for x in range(40, 5, -3):
    print(x)
ex = list(range(40, 10, -4))
print(ex)'''

# функция sum(сумма)
'''mln = list(range(0, 500, 50))
print(mln)
print(sum(mln))'''

# открытие файла(open)
'''textFile = open('D:\\work\\Pyton\\text.txt')
text = textFile.read()
print(text)'''

# запись в файл(write) и его открытие(open)
'''textFile1 = open('D:\\work\\Pyton\\text1.txt',"w")
textFile1.write('что то крякает жабокряк yes')
textFile1.close()
textFile1 = open('D:\\work\\Pyton\\text1.txt')
print(textFile1.read())'''

'''chifr = ("этот если способ вы плохо это подходит читаете, для что-то шифрования пошло важных не сообщений так,")
mass = chifr.split()
print(mass[1],mass[3], mass[5], mass[7], mass[9], mass[11], mass[13], mass[15],
      mass[0], mass[2], mass[4], mass[6], mass[8], mass[10])'''

'''textFile = open('D:\\work\\Pyton\\text.txt')
optextFile = textFile.read()
print(optextFile)
optextFile = open('D:\\work\\Pyton\\text.txt', "w")
optextFile.write('vika')
optextFile.close()
new = open('D:\\work\\Pyton\\text.txt')
print(new)'''

# модуль сору(скопировать)
'''import copy
class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
harry = Animal('гираф', 6, 'фиолетовый')
carry = Animal('фираф', 9, 'оранж')
byllu = Animal('пердунаф', 12,'беллый')
myAnimals = [harry, carry, byllu]
moreAnimals = copy.deepcopy(myAnimals)
print(myAnimals[0].species)
print(moreAnimals[0].species)
myAnimals[0].species = 'вампир'
print(myAnimals[0].species)
print(moreAnimals[0].species)
sally = Animal('сфинкс', 4, 'песочный')
myAnimals.append(sally)
print(len(myAnimals))
print(len(moreAnimals))
print(myAnimals[3].color)'''

# модуль keyword(ключевые слова)
'''import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('hdkjh'))
print(keyword.kwlist)'''

# Работа со временем и модуль time(время)
'''import time
print(time.time())
def lotOFtime(max):
    t1 = time.time()
    for x in range (0, max):
        print(x)
    t2 = time.time()
    print(f'прошло секунд:c {t2 - t1}')
lotOFtime(100)'''

# Преобразование дат с помощью asctime(узнать время)
'''import time
print(time.asctime())

t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))'''

# Получаем дату и время с помощью localtime(местное время)
'''import time
print(time.localtime())
t = time.localtime()
year = t[0]
month = t[1]
print(f"{month} месяц {year} год")'''

# Делаем задержку с помощью sleep(сон)
'''import time
for a in range(1, 10):
    print(a)
    time.sleep(1)'''

# Модуль pickle(засолить) и сохранение информации
'''import  pickle
game_data = {'позиция-игрока' : 'С23 В45',
             'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
             'рюкзак' : ['веревка', 'молоток', 'яблоко'],
             'деньги' : 158.50}
save = open('save.dat', 'wb')
pickle.dump(game_data, save)
save.close()

load = open('save.dat', 'rb')
loaded = pickle.load(load)
load.close()
print(loaded)'''

'''#Модуль Turtle(рисовалка черепаха)
import turtle
turtle.speed(1)
t = turtle.Pen()

anny = turtle.Pen()
katy = turtle.Pen()
petty = turtle.Pen()
sanny = turtle.Pen()
anny.forward(80)
anny.left(90)
anny.forward(50)
anny.right(90)
anny.forward(70)
katy.forward(100)
katy.left(90)
katy.forward(17)
katy.right(90)
katy.forward(50)
petty.forward(80)
petty.right(90)
petty.forward(50)
petty.left(90)
petty.forward(70)
sanny.forward(100)
sanny.right(90)
sanny.forward(17)
sanny.left(90)
sanny.forward(50)
turtle.done()'''

'''avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
turtle.done()'''

'''t.reset()
for x in range(1, 5):
    t.forward(50)
    t.left(90)'''

'''t.reset()
for x in range (1, 9):
    t.forward(100)
    t.left(225)'''

'''t.reset()
for x in range(1 ,38):
    t.forward(100)
    t.left(95)'''

'''t.reset()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)'''
#Begin fill — начать заполнение
#End fill — закочить заполнение

'''t.reset()
t.color(0, 0, 0)
t.begin_fill()
t.circle(50)
t.end_fill()'''

'''def my_cyrcle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    turtle.done()
print(my_cyrcle(0, 0, 0))'''

'''def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
print(mysquare(25, True))
print(mysquare(50, True))
print(mysquare(75, True))
print(mysquare(100, True))
print(mysquare(125, True))'''

'''def mystar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
t.color(0.9, 0.75, 0)
print(mystar(120, True))
t.color(0,0,0)
print(mystar(120, False))
turtle.done()'''

'''def figure(step, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(step)
        t.right(45)
    if filled == True:
        t.end_fill()
t.color(0.9, 0.75, 0)
print(figure(50, True))
t.color(0,0,0)
print(figure(50, False))
turtle.done()'''

'''def draw_star(size, points):
    t.color(1, 0.5, 0.5)
    t.begin_fill()
    for x in range(1, points):
        t.forward(size)
        if x % 2 == 0:
            t.left(55)
        else:
            t.right(125)
    t.end_fill()
print(draw_star(80, 11))
turtle.done()'''

'''def parity(number):
    result = "odd"                              # Function body
    if number % 2 == 0:
        result = "even"                         # Body of if-block
    return result                               # Not part of if-block

for num in range(4):                            # Not part of function
    print("Number", num, "is", parity(num))     # Body of for-loop
print("This is not part of the loop")'''

#преобразовать число 25 из десятичной системы в шестнадцатеричную
'''print('%x' % 25)'''

#модуль Tkinter  для работы с графикой
'''def hello():
    print('привет')
from tkinter import *
tk = Tk()
btn = Button(tk, text="нажми меня", command=hello)
btn.pack()
tk.mainloop()'''

'''def person(width, height):
    print(f'моя ширина {width}, а моя высота {height}')
person(5, 180)'''


'''from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
random_rectangle(400, 400, 'green')
random_rectangle(400, 400, 'red')
random_rectangle(400, 400, 'blue')
random_rectangle(400, 400, 'orange')
random_rectangle(400, 400, 'yellow')
random_rectangle(400, 400, 'pink')
random_rectangle(400, 400, 'purple')
random_rectangle(400, 400, 'violet')
random_rectangle(400, 400, 'magenta')
random_rectangle(400, 400, 'cyan')
tk.mainloop()'''


'''from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
def random_poligon(width, height, long, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    z1 = random.randrange(long)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    z2 = random.randrange(z1 + random.randrange(long))
    canvas.create_polygon(x1, x2, y1, y2, z1, z2, fill=fill_color)

random_poligon(400, 400, 400, 'green')
random_poligon(400, 400, 400, 'red')
random_poligon(400, 400, 400, 'blue')
random_poligon(400, 400, 400, 'orange')
random_poligon(400, 400, 400, 'yellow')
random_poligon(400, 400, 400, 'pink')
random_poligon(400, 400, 400, 'purple')
random_poligon(400, 400, 400, 'violet')
random_poligon(400, 400, 400, 'magenta')
random_poligon(400, 400, 400, 'cyan')
tk.mainloop()'''


'''from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)
tk.mainloop()'''

'''from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(100, 100, 300, 100, 300, 300, fill="white", outline="green")
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="blue", outline="black")
canvas.create_text(150, 100, text='Был один человек из Тулузы,')
canvas.create_text(130, 120, text='Что сидел на огромном арбузе.', fill='red')
canvas.create_text(150, 150, text='Он сказал: "Это ужас,', font=('Times', 15))
canvas.create_text(200, 200, text='Но бывает и хуже:', font=('Helvetica', 20))
canvas.create_text(220, 250, text='Вон мой братец сидит', font=('Courier', 22))
canvas.create_text(220, 300, text='На медузе".', font=('Courier', 30))

tk.mainloop()'''

'''import time
import random
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
my_image = PhotoImage(file='D:\\i.gif')
canvas.create_image(200, 200, anchor=NW, image=my_image)


for bzic in range(0, 20):
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    for zic in range(0, 5):
         canvas.move(1, x, y)
         tk.update()
         time.sleep(0.1)

tk.mainloop()'''

'''import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
v'''

'''import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 150):
    canvas.move(1, 1, 0)
    tk.update()
    time.sleep(0.01)
for x in range(0, 150):
    canvas.move(1, 0, 1)
    tk.update()
    time.sleep(0.01)
for x in range(0, 150):
    canvas.move(1, -1, 0)
    tk.update()
    time.sleep(0.01)
for x in range(0, 150):
    canvas.move(1, 0, -1)
    tk.update()
    time.sleep(0.01)
tk.mainloop()'''

'''from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.move(mytriangle, 5, 0)
canvas.itemconfig(mytriangle, fill='blue')
canvas.itemconfig(mytriangle, outline='red')
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(1, 5, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()'''

'''from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
def movetriangle(event):
    canvas.move(1, 5, 0)
canvas.bind_all('<KeyPress-Return>', movetriangle)
tk.mainloop()'''

#ключевые слова в Python
#and
'''age = 21
if age >= 10 and age <= 20:
    print("осторожно подросток")
elif age > 20:
    print(" старикан")
else:
    print("писюн малолетка")'''

#as(периименовать модуль в более короткий)
'''import i_am_a_python_module_that_is_not_very_useful as notuseful
notuseful.do_something()
Я сделал что-то бесполезное.
notuseful.do_something_else()
Я сделал еще что-то бесполезное!'''

#assert позволяет убедиться, что некое выражение дает True
'''number  = 10
assert  number < 5'''

#break служит для остановки и досрочного выхода из цикла
'''import time
age = 10
for x in range(1, 100):
    time.sleep(1)
    print(f'отсчет ' + str(x))
    if x == age:
        print('закончили считать')
        break'''

#class служит для определения типов сущностей (классов), таких как «средство передвижения», «животное», «человек».
#У каждого класса может быть специальная функция __init__, предназначенная для подготовки новых объектов к работе.
#Например, если объектам класса Car нужно свойство color, его можно добавить в функции __init__,
#которая вызывается при создании объекта

'''class Car:
    def __init__(self, color):
        self.color = color
        car1 = Car('red')
        car2 = Car('blue')
        print(car1)'''

#continue позволяет «перескочить» к следующему повтору цикла, так что следующая после continue часть тела цикла будет
#пропущена. В отличие от break происходит не выход из цикла, а досрочное завершение текущего повтора с переходом к следующему.
# Например,если у нас есть список строк и мы хотим напечатать все элементы, которые начинаются не с буквы «б»,
# можно написать такой код

'''my_items = ['apple', 'orange', 'banane', 'chery']
for item in my_items:
    if item.startswith('b'):
        continue
    print(item)'''

#def it is function
'''def minutes(year):
    return year * 365 * 24 * 60
print(minutes(10))'''

#del удалить елемент списка или словаря
'''what_i_want = ['радиоуправляемый автомобиль', 'новый велосипед', 'компьютерная игра']
del what_i_want[2]
what_i_want.append('змея-робот')
print(what_i_want)'''

#elif(ещё если) Ключевое слово elif используется как часть конструкции if (см. описание ключевого слова if).
#else(ещё) Ключевое слово else используется как часть конструкции if (см. описание ключевого слова if)

#Ключевое слово if(если) нужно для выполнения кода в соответствии с заданным условием.
# Совместно с if также используются ключевые слова else и elif (сокращение от else if)

'''toy_price = 100
if toy_price > 1000:
    print('Эта игрушка чересчур дорогая')
elif toy_price > 100:
    print('Эта дорогая игрушка')
else:
    print('Я могу купить эту игрушку')'''

#import используется для загрузки (импортирования)
#модуля в программу. Например, следующая команда загружает модуль
#sys, после чего им можно пользоваться

#import sys

#in используется в логических выражениях для проверки, входит ли некое значение в набор элементов.
#Например, есть ли среди элементов списка число 1

'''if 1 in [1,2,3,4]:
    print('число есть в списке')'''

'''clothing_list = ['шорты', 'трусики', 'боксеры', 'кальсоны',
'панталоны']
    if 'штаны' in clothing_list:
        print('штаны есть в списке')
    else:
        print('штанов в списке нет')'''

#is(есть) по смыслу похоже на оператор «равно» (==), который используется для проверки равенства двух значений
#print(10 is 10)

#lambda используется для создания безымянных или «встроенных» функций. Мы не рассматриваем безымянные функции
#в этой книге

#not
#Если утверждение истинно, ключевое слово not сделает его ложным. Например, если создать переменную x и задать
#ей значение True, а затем напечатать значение x, поставив перед ним not, выйдет вот что
'''x = True
print(not x)'''
#Ключевое слово not кажется бесполезным до тех пор, пока вы не начнете использовать not вместе с if.
#Например, проверить, что строка не находится в списке, можно так:

'''clothing_list = ['шорты', 'трусики', 'боксеры', 'кальсоны', 'панталоны']
if 'штаны' not in clothing_list:
    print('Как вы живете без штанов?')'''

#or(или) обозначается операция «логическое ИЛИ». Ее используют для объединения двух булевых (то есть возвращающих True
#или False) выражений. Составное выражение даст True, если хотя бы одно из исходных выражений дает True
'''dino = 'Аллозавр' 
if dino == 'Тираннозавр' or dino == 'Аллозавр':
    print('Хищники')
elif dino == 'Анкилозавр' or dino == 'Апатозавр':
    print('Травоядные')'''

# pass(пропустить) и код запустится, несмотря на то что он не завершен
'''for x in range(0, 7):
    print(f'x = {x}')
    if x == 5:
        pass'''

#raise(поднять) С помощью ключевого слова raise можно вызвать ошибку в программе.
#Как ни странно, в продвинутом программировании это часто бывает полезным. В этой книге команда raise не рассматривается.

#return(вернуть) используется для возвращения значения из функции. Например, можно создать функцию,
# которая вычисляет количество секунд, прожитых вами до последнего дня рождения

'''def age_in_second(age_in_year):
    return age_in_year * 365 * 60 * 60
print(age_in_second(12))'''

#try(попробовать) открывает блок кода, который заканчивается ключевыми словами except и finally.
#Блоки try/except/finally используются для обработки ошибок (например, чтобы показывать пользователю понятное
#сообщение, а не ошибку Python). В этой книге ключевое слово try не рассматривается\

#while(пока) цыкл напоминает for, однако если for перебирает значения из заданного диапазона, то while повторяется до тех пор,
#пока условие дает True. Будьте осторожны: если условие цикла while всегда будет выполняться, программа не выйдет
#из цикла (это называется бесконечным циклом), пока вы ее не остановите, нажав Ctrl-C. Например:

'''x = 1
while x == 1:
    print('Привет')'''

'''x = 1
while x < 10:
    print('Привет')
    x = x + 1
'''

#with(c) используется для создания блоков кода с обработкой ошибок наподобие блоков try/finally.
#В этой книге команда withне рассматривается.

#yield(создавать) по смыслу напоминает return, но используется со специальным классом объектов — генераторами.
#Генераторы создают значения «на лету» (то есть по запросу), и функция range работает как генератор.
#В этой книге команда yield не рассматривается.






