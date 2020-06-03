from smbus import SMBus
from tkinter import *
import tkinter.font

address = 8
bus = SMBus(1)
win = Tk()
win.title("I2C LED's")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12)

def Led1():
    bus.write_byte(address, 0)
    print ("RED LED ON")
def Led1_2():
    bus.write_byte(address, 1)
    print ("RED LED OFF")
def Led2():
    bus.write_byte(address, 2)
    print ("Blue LED ON")
def Led2_1():
    bus.write_byte(address, 3)
    print ("Blue LED OFF")
def Quit():
    bus.write_byte(address, 1)
    bus.write_byte(address, 3)
    win.destroy()

ledButton = Button(win, text = 'Turn Red Led ON', font = myFont, command = Led1, bg = 'bisque2', height = 1, width = 50)
ledButton.grid(row=0, column=1)
ledButton = Button(win, text = 'Turn Red Led OFF', font = myFont, command = Led1_2, bg = 'bisque2', height = 1, width = 50)
ledButton.grid(row=1, column=1)
ledButton1 = Button(win, text = 'Turn Blue Led ON', font = myFont, command = Led2, bg = 'bisque2', height = 1, width = 50)
ledButton1.grid(row=2, column=1)
ledButton1 = Button(win, text = 'Turn Blue Led OFF', font = myFont, command = Led2_1, bg = 'bisque2', height = 1, width = 50)
ledButton1.grid(row=3, column=1)
QUIT = Button(win, text = 'QUIT', font = myFont, command = Quit, bg = 'bisque2', height = 1, width = 50)
QUIT.grid(row=4, column=1)
