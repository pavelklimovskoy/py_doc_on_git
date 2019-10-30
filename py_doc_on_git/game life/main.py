from tkinter import *

screen_size_x = 1000
screen_size_y = 700
cell_size = 10
size_x = screen_size_x // cell_size
size_y = screen_size_y // cell_size
cells = [[0 for i in range(size_y)] for j in range(size_x)]
next_gen = [[0 for i in range(size_y)] for j in range(size_x)]
delay = 0.01
flag = 1
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def get_n(x, y):
    n = 0
    for i in range(8):
        n += cells[(x + dx[i]) % size_x][(y + dy[i]) % size_y]
    return n


def draw_red(x, y):
    x *= cell_size
    y *= cell_size
    cvs.create_rectangle(x, y, x + cell_size, y + cell_size, fill="red", outline="black")


def draw_white(x, y):
    x *= cell_size
    y *= cell_size
    cvs.create_rectangle(x, y, x + cell_size, y + cell_size, fill="white", outline="black")


def click_l(event):
    x, y = event.x // cell_size, event.y // cell_size
    cells[x][y] = 1
    next_gen[x][y] = 1
    draw_red(x, y)


def click_r(event):
    x, y = event.x // cell_size, event.y // cell_size
    cells[x][y] = 0
    next_gen[x][y] = 0
    draw_white(x, y)


def activation(x, y):
    cells[x][y] = 1
    draw_red(x, y)


def deactivation(x, y):
    cells[x][y] = 0
    draw_white(x, y)


def draw_grid():
    for i in range(0, screen_size_x, cell_size):
        cvs.create_line(i, 0, i, screen_size_y)
        cvs.create_line(0, i, screen_size_x, i)


def stop():
    global flag
    flag = 0


def start():
    global flag
    flag = 1
    simulation()


def reset():
    for x in range(size_x):
        for y in range(size_y):
            cells[x][y] = 0
            next_gen[x][y] = 0
            draw_white(x, y)


def save():
    file = open("cells", "w")
    file.write("screen_size_x = " + str(screen_size_x) + "\n")
    file.write("screen_size_y = " + str(screen_size_y) + "\n")
    file.write("cell_size = " + str(cell_size) + "\n")
    for line in cells:
        for c in line:
            file.write(str(c) + " ")
        file.write("\n")
    file.write("\n")
    file.close()


def simulation():
    if not flag:
        return 0
    for i in range(size_x):
        for j in range(size_y):
            if not cells[i][j]:
                n = get_n(i, j)
                if n == 3:
                    next_gen[i][j] = 1
    for i in range(size_x):
        for j in range(size_y):
            if cells[i][j]:
                n = get_n(i, j)
                if n > 3 or n < 2:
                    next_gen[i][j] = 0
    for i in range(size_x):
        for j in range(size_y):
            if cells[i][j] != next_gen[i][j]:
                if next_gen[i][j]:
                    activation(i, j)
                else:
                    deactivation(i, j)
    root.after(int(delay * 1000), simulation)


root = Tk()
root.title('game "life"')
root.geometry(str(screen_size_x) + "x" + str(screen_size_y))
root.resizable(width=False, height=False)
root.configure(background='white')
cvs = Canvas(root, width=screen_size_x, height=screen_size_y, bg="white")
cvs.pack(side=TOP)
panel = Menu(root,  background='white', activebackground='red', activeforeground='white')
root.config(menu=panel)
root.bind('<Button-1>', click_l)
root.bind('<Button-3>', click_r)
panel.add_command(label='Start', command=start)
panel.add_command(label='Stop', command=stop)
panel.add_command(label='Reset', command=reset)
panel.add_command(label='Save', command=save)
draw_grid()
root.mainloop()
