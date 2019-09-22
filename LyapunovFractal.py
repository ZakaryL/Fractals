import tkinter as tk
from time import sleep
import math


def tohex(a):
    t = str(hex(a)[2:4])
    if len(t) == 1:
        t = "0" + t
    return t


def draw(line):
    for i in range(len(line)):
        e = line[i][0]
        if e > 0:
            hi = 1
            h = 60
        else:
            hi = 4
            h = 240
        vm = (100 - (e % 100))*((e/100) % 100)/100
        a = int((100-vm) * ((h % 60) / 60))
        vi = vm + a
        vd = ((e/100) % 100) - a
        a = int((e/100) % 100)
        b = int((vi * 255) / 100)
        w = int((vd * 255) / 100)
        f = int((vm * 255) / 100)
        if hi == 0:
            t = tohex(b)
            r = tohex(a)
            q = tohex(f)
            color = "#" + r + t + q
        elif hi == 1:
            t = tohex(w)
            r = tohex(a)
            q = tohex(f)
            color = "#" + t + r + q
        elif hi == 2:
            t = tohex(b)
            r = tohex(a)
            q = tohex(f)
            color = "#" + q + r + t
        elif hi == 3:
            t = tohex(w)
            r = tohex(a)
            q = tohex(f)
            color = "#" + q + t + r
        elif hi == 4:
            t = tohex(b)
            r = tohex(a)
            q = tohex(f)
            color = "#" + t + q + r
        else:
            t = tohex(w)
            r = tohex(a)
            q = tohex(f)
            color = "#" + r + q + t
        img.put(color, (line[i][1][0], line[i][1][1]))
        # c.create_rectangle(line[i][1][0], line[i][1][1], line[i][1][0]+2, line[i][1][1]+2, fill=color, outline=color)


def limit(line, a, b):
    xn = 0.5
    rn = 0
    lim = 0
    for i in range(1, 10**3):
        # print(i%2)
        if line[i % len(line)] == "A":
            rn = a
        else:
            rn = b
        xn = rn*xn*(1-xn)
        r = math.fabs(rn*(1-2*xn))
        if r != 0:
            lim = lim + math.log(r)
    if lim > 10**5:
        lim = 10**5
    elif lim < -10**5:
        lim = -10**5
    return lim


def start(event):
    global run
    run = not run
    t = []
    line = "AB"
    x_lim = size_x
    y_lim = size_y
    i = 2/x_lim
    j = 2/y_lim
    print(i, j)
    a, b = 2, 2
    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:
        for x in range(0, size_x):
            for y in range(0, size_y):
                lim = limit(line, a, b)
                t.append((lim, (x, y)))
                a = a + i
            b = b + j
            a = 2
        draw(t)
        t.clear()
        mainwindow.update()
        run = not run

        sleep(.3)


mainwindow = tk.Tk()
size_x = 500
size_y = 500
c = tk.Canvas(width=size_x, height=size_y)
img = tk.PhotoImage(width=size_x, height=size_y)
c.pack()
c.create_image((size_x/2, size_y/2), image=img, state="normal")
cBlue = "#0000FF"
cWhite = "#FFFFFF"
cRed = "#FF0000"
run = False
btn = tk.Button(text="Start Game")
btn.bind("<Button>", start)
btn.pack(side="left")
tk.mainloop()

