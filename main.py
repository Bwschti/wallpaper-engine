import os
import tkinter as tk
import PIL
from tkinter import*
import ctypes
import sys

import tkinter.filedialog
filename = tkinter.filedialog.askopenfilename()

WALLPAPER_PATH = filename
ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)
input("Ready")

im = PIM.open("C:\\...\\CeEOy.gif")
ph = ImageTk.PhotoImage(im)
gif = Label(root, image = ph, bg="black", bd=3)
gif.image = ph
framnr = 79
frames = [PhotoImage(file="C:\\...\\CeEOy.gif",
                format = 'gif -index %i' %(i)) for i in range(framnr)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind>78: 
         ind = 0
    gif.configure(image = frame)
    root.after(100, update, ind)
    
gif = Label(root)
gif.pack()
root.after(0, update, 0)
root.mainloop()