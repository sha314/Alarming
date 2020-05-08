#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this example, we use the pack
manager to create a review example.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
import tkinter as tk
from PIL import Image, ImageTk
import os

ICON_PATHS={
    "delete":"../resources/icon/png/delete.png",
    "reset":"../resources/icon/png/reset.png",
    "start":"../resources/icon/png/start.png",
    "stop":"../resources/icon/png/stop.png",
}


def main():
    root = Tk()

    root.geometry("400x400+300+300")
    # root.iconbitmap('../resources/png/icon.ico') # main icon
    root.iconphoto(False, tk.PhotoImage(file=r'../resources/icon/png/stop.png')) # or this

    frame = Frame(root)
    btn = Button(frame, width=5)

    photo = tk.PhotoImage(file=r"../resources/icon/png/delete.png")
    # # btn_start_timer['image'] = photo.subsample(1, 1) # Resizing image to fit on button
    icon = photo.subsample(2, 2)  # Resizing image to fit on button
    btn.config(image=icon)
    btn.pack()
    frame.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
    # os.listdir("../")