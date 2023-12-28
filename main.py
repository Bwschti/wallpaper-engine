import ctypes
import sys

import tkinter.filedialog
filename = tkinter.filedialog.askopenfilename()

WALLPAPER_PATH = filename
ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)
input("Ready")