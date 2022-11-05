from tkinter import *
from tkinter import messagebox

root = Tk()

# название
root.title("Крестики-нолики")

# запрет изменение окна
root.resizable(0, 0)

# размещение окна по центру
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 4
root.wm_geometry("+%d+%d" % (x, y))


# функция кнопки "Заново"
def rtrn():
    global game_over
    global cells
    game_over = 0

    for y_num in range(y_count):
        for x_num in range(x_count):
            cells[y_num][x_num] = -1

    canv.delete("game")


# Функция кнопки "Как играть"
def help():
    messagebox.showinfo("Как играть", "Выиграет тот, у кого 5 подряд Х или О")


# Функция кнопки "Создатели"
def aboutme():
    messagebox.showinfo("Создатели",
                        "Создатель - Гадимов Наби Мехманович\nСтудент 1 курса КГУ и просто хороший человек")


# =========================================================игра=======================================================

# формирование поля
cell_size = 24
x_count = 10
y_count = 10
i = 0

# признак окончания игры
game_over = 0

# массив результатов ходов
cells = []
for y_num in range(y_count):
    row = []
    for x_num in range(x_count):
        row.append(-1)
    cells.append(row)

# формирование канвы
canv_width = x_count * cell_size
canv_height = y_count * cell_size

canv = Canvas(root, width=canv_width, height=canv_height)
canv.pack()

# формирование клеточек
for x_num in range(x_count):
    for y_num in range(y_count):
        canv.create_line(0, y_num * cell_size, canv_width, y_num * cell_size)
        canv.create_line(x_num * cell_size, 0, x_num * cell_size, canv_height)


# функция подсчета значений на линии
def calc_line(y_num, x_num, y_step, x_step):
    val = cells[y_num][x_num]

    val_count = 0
    for num in range(5):
        if cells[y_num + num * y_step][x_num + num * x_step] == val:
            val_count += 1
        else:
            break
    for num in range(1, 5):
        if cells[y_num - num * y_step][x_num - num * x_step] == val:
            val_count += 1
        else:
            break
    return val_count


# функиця подсчета значений на всех линиях около клетки
def calc_result(y_num, x_num):
    global game_over
    val_counts = []
    val_count = calc_line(y_num, x_num, 0, 1)
    val_counts.append(val_count)
    val_count = calc_line(y_num, x_num, 1, 1)
    val_counts.append(val_count)
    val_count = calc_line(y_num, x_num, 1, 0)
    val_counts.append(val_count)
    val_count = calc_line(y_num, x_num, -1, 1)
    val_counts.append(val_count)
    val_count = max(val_counts)

    if val_count >= 5:
        game_over = 1
        if cells[y_num][x_num] == 0:
            st = "0 - ВЫИГРАЛ"
        else:
            st = "X - ВЫИГРАЛ"
        st1 = "Нажмите ENTER для новой игры"
        canv.create_text(280, 80, text=st1, font=("Arial", 20), tag='game')
        messagebox.showinfo("Конец игры", st)


# функция отрисовки нолика
def draw_oval(event):
    global cells
    x_num = event.x // cell_size
    y_num = event.y // cell_size
    if cells[y_num][x_num] == -1 and not game_over:
        cells[y_num][x_num] = 0
        x_left = x_num * cell_size + 3
        y_top = y_num * cell_size + 3
        canv.create_oval(x_left, y_top, x_left + cell_size - 6, y_top + cell_size - 6, outline="#050", width=3,
                         tag='game')
        calc_result(y_num, x_num)
    canv.bind('<Button-1>', draw_krest)


# функция отрисовки крестика
def draw_krest(event):
    global cells
    x_num = event.x // cell_size
    y_num = event.y // cell_size
    if cells[y_num][x_num] == -1 and not game_over:
        cells[y_num][x_num] = 1
        x_left = x_num * cell_size + 3
        y_top = y_num * cell_size + 3
        canv.create_line(x_left, y_top, x_left + cell_size - 6, y_top + cell_size - 6, fill='blue', width=3, tag='game')
        canv.create_line(x_left + cell_size - 6, y_top, x_left, y_top + cell_size - 6, fill='blue', width=3, tag='game')
        calc_result(y_num, x_num)
    canv.bind('<Button-1>', draw_oval)


canv.bind('<Button-1>', draw_krest)


# включить обработчик клавиатуры
def key_handl(event):
    # обработать нажатия клавиш
    global game_over
    global cells
    if event.keysym == "Return" and game_over:  # начать игру заново
        game_over = 0

        for y_num in range(y_count):
            for x_num in range(x_count):
                cells[y_num][x_num] = -1

        canv.delete("game")


canv.bind("<KeyPress>", key_handl)
canv.focus_set()

# создание меню
mainmenu = Menu(root)
root.config(menu=mainmenu)

# режим игры
choice = Menu(mainmenu, tearoff=0)
choice.add_command(label="2 человека")
choice.add_command(label="С компьютером")

# справка
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Как играть", command=help)
helpmenu.add_command(label="Создатели", command=aboutme)

# панель
mainmenu.add_cascade(label="Режим игры", menu=choice)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
mainmenu.add_command(label='Заново', command=rtrn)

# запустить игру
root.mainloop()