import tkinter as tk
from time import sleep


def draw(line):
    n = 2
    vec = [n, 0]
    coord = [size_x*0.1, size_y*0.65]
    for i in range(len(line)):
        if i % 2 == 0:
            if line[i] == "0":
                c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed)
                coord[0] = coord[0] + vec[0]
                coord[1] = coord[1] + vec[1]
                if vec[1] == 0:
                    if vec[0] > 0:
                        vec = [0, n]
                    else:
                        vec = [0, -n]
                else:
                    if vec[1] > 0:
                        vec = [n, 0]
                    else:
                        vec = [-n, 0]
            else:
                c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed)
                coord[0] = coord[0] + vec[0]
                coord[1] = coord[1] + vec[1]
        else:
            if line[i] == "0":
                c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed)
                coord[0] = coord[0] + vec[0]
                coord[1] = coord[1] + vec[1]
                if vec[1] == 0:
                    if vec[0] > 0:
                        vec = [0, -n]
                    else:
                        vec = [0, n]
                else:
                    if vec[1] > 0:
                        vec = [-n, 0]
                    else:
                        vec = [n, 0]
            else:
                c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed)
                coord[0] = coord[0] + vec[0]
                coord[1] = coord[1] + vec[1]
        mainwindow.update()


def fib(n):
    if n == 0:
        return "1"
    if n == 1:
        x1 = "0"
        return x1
    else:
        return fib(n-1) + fib(n-2)


def start(event):
    global run
    run = not run
    line = fib(20)
    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:

        draw(line)

        sleep(.3)


mainwindow = tk.Tk()
size_x = 900
size_y = 600
c = tk.Canvas(width=size_x, height=size_y)
c.pack()
cBlue = "#0000FF"
cWhite = "#FFFFFF"
cRed = "#FF0000"
run = False
btn = tk.Button(text="Start Game")
btn.bind("<Button>", start)
btn.pack(side="left")
tk.mainloop()

