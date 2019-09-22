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
    n = 1
    vec = [0, -n]
    coord = [size_x*0.5, size_y*1]
    stack = []
    for i in line:
        if i == "F" or i == "X":
            c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed, width=1)
            coord[0] = coord[0] + vec[0]
            coord[1] = coord[1] + vec[1]
        elif i == "[":
            stack.append(((coord[0], coord[1]), (vec[0], vec[1])))
            vec[0], vec[1] = matmult(vec[0], vec[1], "+")
        else:
            j = len(stack)-1
            coord[0] = stack[j][0][0]
            coord[1] = stack[j][0][1]
            vec[0] = stack[j][1][0]
            vec[1] = stack[j][1][1]
            stack.pop(j)
            vec[0], vec[1] = matmult(vec[0], vec[1], "-")
        mainwindow.update()
        # sleep(.001)

def fib(line, alf):
    nline = ""
    for i in range(len(line)):
        if line[i] == "F":
            nline = nline + alf["F"]
        elif line[i] == "X":
            nline = nline + alf["X"]
        else:
            nline = nline + line[i]
    return nline


def start(event):
    global run
    run = not run
    alf = {"X": "XX", "F": "X[F]F"}
    line = "F"
    for i in range(9):
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
size_y = 700
alfa = 0.78539816340
si = math.sin(alfa)
co = math.cos(alfa)
c = tk.Canvas(width=size_x, height=size_y)
c.pack()
cBlue = "#0000FF"
cWhite = "#FFFFFF"
cRed = "#FF0000"
cGreen = "#39FF14"
run = False
btn = tk.Button(text="Start Game")
btn.bind("<Button>", start)
btn.pack(side="left")
tk.mainloop()

