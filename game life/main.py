from tkinter import *

width = 1000
height =  800
step = 20
c_width = width // step
c_height = height // step
cells = []
next_gen = []
delay = 1
flag = 1



for x in range(c_width):
    cells.append([])                       #тут
    for y in range(c_height):
        cells[x].append(0)


for x in range(c_width):
    next_gen.append([])                       #тут
    for y in range(c_height):
        next_gen[x].append(0)


def get_n(i, j):
    n = cells[(i - 1) % c_width][(j - 1) % c_height] + \
        cells[(i - 1) % c_width][j] + \
        cells[(i - 1) % c_width][(j + 1) % c_height] + \
        cells[i][(j - 1) % c_height] + \
        cells[i][(j + 1) % c_height] + \
        cells[(i + 1) % c_width][(j - 1) % c_height] + \
        cells[(i + 1) % c_width][j] + \
        cells[(i + 1) % c_width][(j + 1) % c_height]                                #тут
    return n


def click_l(event):
    global step
    x, y = event.x, event.y
    cells[x // step][y // step] = 1
    next_gen[x // step][y // step] = 1
    cvs.create_rectangle(x - x % step, y - y % step, x - x % step + step, y - y % step + step, fill="red", outline="black")


def click_r(event):
    global step
    x, y = event.x, event.y
    cells[x // step][y // step] = 0
    next_gen[x // step][y // step] = 0
    cvs.create_rectangle(x - x % step, y - y % step, x - x % step + step, y - y % step + step, fill="white", outline="black")


def active(x, y):
    global step
    x *= step
    y *= step
    cells[x // step][y // step] = 1
    cvs.create_rectangle(x - x % step, y - y % step, x - x % step + step, y - y % step + step, fill="red", outline="black")


def deactive(x, y):
    global step
    x *= step
    y *= step
    cells[x // step][y // step] = 0
    cvs.create_rectangle(x - x % step, y - y % step, x - x % step + step, y - y % step + step, fill="white", outline="black")


def init_setka(step):
    global width, height
    for i in range(0, width, step):
        cvs.create_line(i, 0, i, height)                                #тут
    for i in range(0, height, step):
        cvs.create_line(0,i,width,i)


def stop():
    global flag
    flag = 0


def start():
    global flag
    flag = 1
    simulation()


def reset():
    for x in range(c_width):
        for y in range(c_height):                                #тут
            cells[x][y] = 0

    for x in range(c_width):
        for y in range(c_height):                                #тут
            next_gen[x][y] = 0

    for x in range(c_width):
        for y in range(c_height):
            deactive(x, y)


def save():
    file = open("cells", "w")
    file.write("width = " + str(width) + "\n")
    file.write("height = " + str(height) + "\n")
    file.write("step = " + str(step) + "\n")
    for line in cells:
        for c in line:
            file.write(str(c) + " ")
        file.write("\n")
    file.write("\n")
    file.close()






def simulation():
    global  step, width, height, c_width, c_height, flag
    if flag:
        for i in range(c_width):
            for j in range(c_height):
                n = get_n(i, j)
                if not cells[i][j]:
                    if n == 3:
                        next_gen[i][j] = 1
        for i in range(c_width):
            for j in range(c_height):
                n = get_n(i, j)
                if cells[i][j]:
                    if n > 3 or n < 2:
                        next_gen[i][j] = 0
        for i in range(c_width):
            for j in range(c_height):
                if cells[i][j] != next_gen[i][j]:
                    if next_gen[i][j]:
                        active(i, j)
                    else:
                        deactive(i, j)
    else:
        return 0

    root.after(100, simulation)


root = Tk()
root.title("game \"life\" ")
root.geometry(str(width)+"x"+str(height))
root.resizable(width=False, height=False)
root.configure(background='white')

cvs = Canvas(root, width=width, height=height, bg="#fff")
cvs.pack(side=TOP)

root.bind('<Button-1>', click_l)
root.bind('<Button-3>', click_r)

panel = Menu(root,  background='white', activebackground='red', activeforeground='white')
root.config(menu=panel)

game_menu = Menu(panel, tearoff=0,  background='white', foreground='black', activebackground='red', activeforeground='white')

panel.add_command(label='Start', command=start)
panel.add_command(label='Stop', command=stop)
panel.add_command(label='Reset', command=reset)
panel.add_command(label='Save', command=save)


init_setka(step)

print(cells)

root.mainloop()

