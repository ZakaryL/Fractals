import tkinter as tk
from time import sleep
import math
import copy


def draw(lines):
    t = len(lines)-1
    for i in range(t):
        c.create_line(lines[i][0], lines[i][1], lines[i+1][0], lines[i+1][1], fill=cRed, width=1)
    c.create_line(lines[t][0], lines[t][1], lines[0][0], lines[0][1], fill=cRed, width=1)


def matmult(x, y):
    temp = x*si + y*co
    x = x*co - y*si
    y = temp
    return x, y


def start(event):
    global run
    run = not run
    st_coord = (size_x - (size_x * 0.05), size_y - (size_y * 0.05))
    squad = []
    squad.append(st_coord)
    squad.append((st_coord[0] - (size_x * 0.9), st_coord[1]))
    squad.append((st_coord[0] - (size_x * 0.9), st_coord[1] - (size_y * 0.9)))
    squad.append((st_coord[0], st_coord[1] - (size_y * 0.9)))
    temp = []
    diff_x = (squad[0][0] - squad[1][0]) * 0.04
    diff_y = (squad[1][1] - squad[2][1]) * 0.04
    print(squad)
    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:

        draw(squad)
        mainwindow.update()
        temp.clear()
        for j in range(0, len(squad)):
            if j == 0:
                tx, ty = squad[j][0] - diff_x, squad[j][1] - diff_y
            elif j == 1:
                tx, ty = squad[j][0] + diff_x, squad[j][1] - diff_y
            elif j == 2:
                tx, ty = squad[j][0] + diff_x, squad[j][1] + diff_y
            elif j == 3:
                tx, ty = squad[j][0] - diff_x, squad[j][1] + diff_y

            temp_x, temp_y = tx - (size_x/2), ty - (size_y/2)
            x, y = matmult(temp_x, temp_y)
            x, y = x + (size_x/2), y + (size_y/2)
            temp.append((x, y))
        # print(diff_x, diff_y)
        diff_x = (temp[0][0] - temp[1][0]) * 0.04
        diff_y = (temp[1][1] - temp[2][1]) * 0.04
        squad.clear()
        squad = copy.deepcopy(temp)
        sleep(.3)


mainwindow = tk.Tk()
size_x = 600
size_y = 600
alfa = math.pi/45
si = math.sin(alfa)
co = math.cos(alfa)
c = tk.Canvas(width=size_x, height=size_y)
c.pack()
cBlue = "#0000FF"
cWhite = "#FFFFFF"
cRed = "#FF0000"
cBlack = "#000000"
run = False
btn = tk.Button(text="Start Game")
btn.bind("<Button>", start)
btn.pack(side="left")
tk.mainloop()

