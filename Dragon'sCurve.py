import tkinter as tk
from time import sleep


def draw(line):
    c.delete("all")
    for i in range(len(line)-1):
        if i!=len(line)-2:
            c.create_line(line[i][0], line[i][1], line[i+1][0], line[i+1][1], fill=cRed, width=1)
        else:
            c.create_line(line[i][0], line[i][1], line[i + 1][0], line[i + 1][1], fill=cBlue, width=1)
        mainwindow.update()


def matmult(x, y):
    temp = x
    x = -y
    y = temp
    return x, y


def start(event):
    global run
    run = not run
    st_coord = (size_x - (size_x * 0.5), size_y - (size_y * 0.75))
    line = []
    line.append(st_coord)
    line.append((st_coord[0], st_coord[1] - 2))
    line.append((st_coord[0] + 2, st_coord[1] - 2))
    if run:
        btn.configure(text="Stop Game")
    else:
        btn.configure(text="Start Game")
    while run:
        st_coord = (line[len(line)-1][0], line[len(line)-1][1])
        r = len(line)
        print(st_coord)
        for j in range(r - 1, 0, -1):
            temp_x, temp_y = line[j][0] - st_coord[0], line[j][1] - st_coord[1]
            x, y = matmult(temp_x, temp_y)
            x, y = x + st_coord[0], y + st_coord[1]
            line.append((x, y))
        draw(line)

        sleep(.3)


mainwindow = tk.Tk()
size_x = 1200
size_y = 750
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

