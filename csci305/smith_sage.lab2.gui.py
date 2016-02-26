import Tkinter
import turtle
import tkSimpleDialog
import re

f = open('cities_locs.txt','r')
city_locs = {}

for line in f.readlines():
    info = re.split('\|',line)
    locs = re.split(',',info[0])
    city = info[1]
    city_locs[city] = (locs[0],locs[1])


root = Tkinter.Tk()
root.withdraw()
frame = Tkinter.Frame(bg='white')
L1 = Tkinter.Label(frame, text='City0')
L1.pack(side ='top')
E1 = Tkinter.Entry(frame, bd =5)
E1.pack(side = 'top')
L2 = Tkinter.Label(frame, text='City1')
L2.pack(side = 'top')
E2 = Tkinter.Entry(frame, bd =5)
E2.pack(side = 'top')
canvas = Tkinter.Canvas(frame, width=631, height=440)
canvas.pack()
frame.pack(fill='both', expand=True)
t = turtle.RawTurtle(canvas)
t.color('red')
screen = t.getscreen()
screen.bgpic('map.gif')

def draw(city0, city1):
    t.up()
    t.goto(citylocs[city0])
    t.down()
    t.goto(citylocs[city1])

def clear():
    t.clear()

root.deiconify()
root.mainloop()
