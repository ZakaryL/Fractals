import tkinter as tk
from time import sleep
import math


def matmult(x, y, sign):
    if sign == "+":
        temp = - x * si + y * co
        x = x * co + y * si
        y = temp
    else:
        temp = x * si + y * co
        x = x * co - y * si
        y = temp
    return x, y


def draw(line):
    n = 5
    vec = [n, 0]
    coord = [size_x*0.05, size_y*0.9]
    for i in line:
        if i == "F":
            c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed)
            coord[0] = coord[0] + vec[0]
            coord[1] = coord[1] + vec[1]
        else:
            vec[0], vec[1] = matmult(vec[0], vec[1], i)
        mainwindow.update()
        sleep(.01)

def fib(line, alf):
    nline = ""
    for i in range(len(line)):
        if line[i] == "F":
            nline = nline + alf["F"]
        else:
            nline = nline + line[i]
    return nline

def start(event):
    global run
    run = not run
    alf = {"F": "F+F−F−F+F"}
    line = "F"
    for i in range(4):
        line = fib(line, alf)
    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:
        draw(line)
        sleep(.3)


mainwindow = tk.Tk()
size_x = 600
size_y = 400
alfa = 1.48
si = math.sin(alfa)
co = math.cos(alfa)
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

