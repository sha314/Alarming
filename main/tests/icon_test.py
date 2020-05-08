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


class TEST2:
    def __init__(self, master):
        self.master = master
        photo = tk.PhotoImage(file=r"../resources/icon/png/delete.png")
        self.icon = photo.subsample(2, 2)  # Resizing image to fit on button
        # self.iconbox = iconbox.IconBox()

    def construct(self):
        frame = tk.Frame(self.master)

        # btn_remove_timer.config(image=icon)
        # btn_remove_timer['image']=icon
        btn_delete = tk.Button(frame)
        # btn_delete['image'] = self.iconbox.get('delete')
        btn_delete['image'] = self.icon
        btn_delete.pack()
        frame.pack(fill=X)


class TEST(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        photo = tk.PhotoImage(file=r"../resources/icon/png/delete.png")
        self.icon = photo.subsample(2, 2)  # Resizing image to fit on button
        # self.iconbox = iconbox.IconBox()

    def add_btn(self):
        frame = tk.Frame(self.master)


        # btn_remove_timer.config(image=icon)
        # btn_remove_timer['image']=icon
        btn = tk.Button(frame)
        # btn['image'] = self.iconbox.get('delete')
        btn['image'] = self.icon
        btn.pack()
        frame.pack(fill=X)


def test_slot():
    root = Tk()

    root.geometry("400x400+300+300")
    # root.iconbitmap('../resources/png/icon.ico') # main icon
    # root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png')) # or this

    app = Slot(root)
    app.set_id(2)
    # app.construct()
    # app.pack()

    # frame2 = Frame(root)
    # frame2.pack(fill=X)
    # photo = tk.PhotoImage(file=r"../resources/icon/png/delete.png")
    # # # btn_start_timer['image'] = photo.subsample(1, 1) # Resizing image to fit on button
    # icon = photo.subsample(3, 3)  # Resizing image to fit on button
    # # btn_remove_timer.config(image=icon)
    # # btn_remove_timer['image']=icon
    # btn = tk.Button(frame2)
    # btn['image'] = icon
    # btn.pack()
    # print(btn)

    root.mainloop()

def test():
    root = Tk()

    root.geometry("400x400+300+300")
    # root.iconbitmap('../resources/png/icon.ico') # main icon
    # root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png')) # or this

    app = TEST2(root)
    app.construct()
    # app.pack()


    # frame2 = Frame(root)
    # frame2.pack(fill=X)
    # photo = tk.PhotoImage(file=r"../resources/icon/png/delete.png")
    # # # btn_start_timer['image'] = photo.subsample(1, 1) # Resizing image to fit on button
    # icon = photo.subsample(3, 3)  # Resizing image to fit on button
    # # btn_remove_timer.config(image=icon)
    # # btn_remove_timer['image']=icon
    # btn = tk.Button(frame2)
    # btn['image'] = icon
    # btn.pack()
    # print(btn)

    root.mainloop()


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
    # test()
    # test_slot()