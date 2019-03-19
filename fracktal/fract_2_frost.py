import random
from tkinter import Tk,Canvas

def draw():
    global x,y

    rand=random.randint(0,5)
    if (rand==0 or rand==1):
        x=(x+x3)/2
        y=(y+y3)/2
        cvs.create_oval(x,y,x,y,width=1,outline="red")
    elif (rand==2 or rand==3):
        x=(x+x2)/2
        y=(y+y2)/2
        cvs.create_oval(x,y,x,y,width=1,outline="green")
    elif (rand==4 or rand==5):
        x=(x+x1)/2
        y=(y+y1)/2
        cvs.create_oval(x,y,x,y,width=1,outline="blue")
    root.after(5,draw)

if __name__ == '__main__':
    root = Tk()

    cvs=Canvas(root,width=900,height=900, bg="#fff")
    cvs.pack()

    x,y=random.randint(0,900),random.randint(0,900)

    x1,y1=420,40
    x2,y2=840,840
    x3,y3=40,840

    draw()
    root.mainloop()
