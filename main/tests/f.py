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


def to_seconds(timestr):
    seconds= 0
    for part in timestr.split(':'):
        seconds= seconds*60 + int(part)
    return seconds


def seconds_to_hhmmss(seconds):
    r = seconds
    timestamp=""

    hr= int(r/3600)
    r=r%3600
    print(r)
    print(hr)

    minute= int(r/60)
    r=r%60
    print(r)
    print(minute)

    return "{:2}:{:2}:{:2}".format(hr,minute,r)


def timer_clicked():
    print("button liecked")
    entered_value = entry_time.get()
    if "hh" in entered_value or "mm" in entered_value or "ss" in entered_value:
        print("value not valid")
        return
    if "h" in entered_value or "m" in entered_value or "s" in entered_value:
        print("time format not implemented")
        return      
    decoded = to_seconds(entered_value)
    print(decoded, " sec")
    # sleep for specified seconds
    # create the class instance
    timer = Timer(decoded)
    timer.start()

    print("while sleeping")
    # time.sleep(2)
    # print("selpt for ", timer.peek() , " sec")

    return decoded



class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Timer")
        self.pack(fill=BOTH, expand=True)

        # Add timer frame
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter Time", width=10)
        lbl1.pack(side=LEFT, padx=10, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(side=LEFT, padx=20, pady=5)
        
        btn_add_timer = tk.Button(frame1, text = 'Add Timer', fg ='red', command=timer_clicked) 
        btn_add_timer.pack(padx=5, pady=5, side=tk.LEFT)


        # monitor frame
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2a = Label(frame2, text="No", width=5)
        lbl2a.pack(side=LEFT, padx=10, pady=5)

        lbl2b = Label(frame2, text="Time", width=10)
        lbl2b.pack(side=LEFT, padx=10, pady=5)

        lbl2c = Label(frame2, text="ETA", width=10)
        lbl2c.pack(side=LEFT, padx=10, pady=5)

        lbl2d = Label(frame2, text="Action", width=10)
        lbl2d.pack(side=LEFT, padx=10, pady=5)


        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():

    root = Tk()
    root.geometry("400x400+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()