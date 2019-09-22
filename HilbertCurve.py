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
    n = 10
    vec = [0, n]
    coord = [size_x*1, size_y*0]
    for i in line:
        if i == "F":
            c.create_line(coord[0], coord[1], coord[0] + vec[0], coord[1] + vec[1], fill=cRed, width=1)
            coord[0] = coord[0] + vec[0]
            coord[1] = coord[1] + vec[1]
        elif i == "+":
            vec[0], vec[1] = matmult(vec[0], vec[1], i)
        elif i == "-":
            vec[0], vec[1] = matmult(vec[0], vec[1], i)
        mainwindow.update()
        sleep(.0001)

def fib(line, alf):
    nline = ""
    for i in range(len(line)):
        if line[i] == "A":
            nline = nline + alf["A"]
        elif line[i] == "B":
            nline = nline + alf["B"]
        else:
            nline = nline + line[i]
    return nline


def start(event):
    global run
    run = not run
    alf = {"A": "-BF+AFA+FB-", "B": "+AF-BFB-FA+"}
    line = "A"
    for i in range(6):
        line = fib(line, alf)
    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:
        draw(line)
        sleep(.3)


mainwindow = tk.Tk()
size_x = 650
size_y = 650
alfa = 1.57079632679
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

