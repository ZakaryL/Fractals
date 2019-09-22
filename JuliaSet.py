import tkinter as tk
from time import sleep
import math
import png


def draw(e, x, y):
    if e == 0:
        return (0, 0, 0)
        # img.put(cBlack, (x, y))
        # c.create_rectangle(x, y, x + 1, y + 1, fill=cBlack, outline=cBlack)
    else:
        hi = round(e/60) % 6
        vi = int(100 * ((e % 60)/60))
        vd = 100 - vi
        a = 255
        b = int((vi * 255)/100)
        c = int((vd * 255)/100)
        if hi == 0:
            t = str(hex(b)[2:4])
            if len(t) == 1:
                t = "0" + t
            color = (a, b, 0)
            # color = "#" + str(hex(a)[2:4]) + t + "0" + str(hex(0)[2:4])
        elif hi == 1:
            t = str(hex(c)[2:4])
            if len(t) == 1:
                t = "0" + t
            color = (c, a, 0)
            # color = "#" + t + str(hex(a)[2:4]) + "0" + str(hex(0)[2:4])
        elif hi == 2:
            t = str(hex(b)[2:4])
            if len(t) == 1:
                t = "0" + t
            color = (0, a, b)
            # color = "#" + "0" + str(hex(0)[2:4]) + str(hex(a)[2:4]) + t
        elif hi == 3:
            t = str(hex(c)[2:4])
            if len(t) == 1:
                t = "0" + t
            color = (0, c, a)
            # color = "#" + "0" + str(hex(0)[2:4]) + t + str(hex(a)[2:4])
        elif hi == 4:
            t = str(hex(b)[2:4])
            if len(t) == 1:
                t = "0" + t
            color = (b, 0, a)
            # color = "#" + t + "0" + str(hex(0)[2:4]) + str(hex(a)[2:4])
        else:
            t = str(hex(c)[2:4])
            if len(t) == 1:
                t = "0" + t
            color = (a, 0, c)
            # color = "#" + str(hex(a)[2:4]) + "0" + str(hex(0)[2:4]) + t
        # c.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)
        # img.put(color, (x, y))
        return color


def limit(a, b):
    it = 0
    ma = 360
    cx = -0.8
    cy = 0.156
    n = 2
    while a*a + b*b < 4 and it < ma:
        temp = (a*a + b*b)**(n/2)*math.cos(n*math.atan2(b, a)) + cx
        b = (a*a + b*b)**(n/2)*math.sin(n*math.atan2(b, a)) + cy
        a = temp
        it = it + 1

    if it == ma:
        return 0
    else:
        return it


def start(event):
    global run
    run = not run

    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:
        imt = []
        for x in range(0, 2000):
            row = ()
            for y in range(0, 2000):
                a = 1.5 * (x - 2000 / 2) / (0.5 * 2000)
                b = (y - 2000 / 2) / (0.5 * 2000)
                lim = limit(a, b)
                row = row + draw(lim, x, y)
                mainwindow.update()
            imt.append(row)
        run = not run
        r = png.from_array(imt, mode="RGB")
        r.save("gr.png")
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
cBlack = "#000000"
run = False
btn = tk.Button(text="Start Game")
btn.bind("<Button>", start)
btn.pack(side="left")
tk.mainloop()

