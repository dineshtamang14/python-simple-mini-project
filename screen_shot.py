import pyautogui
import tkinter as tk
from tkinter.filedialog import *


window = tk.Tk()

canvas1 = tk.Canvas(window, width=400, height=400)
canvas1.pack()


def take_screen_shot():
    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    screen_shot.save(save_path+"_screenshot.png")


button = tk.Button(text="Take a ScreenShot", command=take_screen_shot, font=10)
canvas1.create_window(160, 160, window=button)

window.mainloop()

