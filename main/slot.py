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


class Converters:
    def __init__(self):
        print("Converters.__init__")


    def to_seconds(self, timestr):
        seconds = 0
        for part in timestr.split(':'):
            seconds = seconds * 60 + int(part)
        return seconds

    def seconds_to_hhmmss(self, seconds):
        r = seconds
        timestamp = ""

        hr = int(r / 3600)
        r = r % 3600
        print(r)
        print(hr)

        minute = int(r / 60)
        r = r % 60
        print(r)
        print(minute)

        return "{:2}:{:2}:{:2}".format(hr, minute, r)


class StopwatchSlot(Frame, Converters):

    def __init__(self, root):
        self.root = root
        super(StopwatchSlot, self).__init__(root)
        # super(Frame, self).__init__(master, **options)
        # Frame.__init(master, **options)
        self.slot_count = 0

        self.pady = 2
        self.padxs  = [1, 2, 15, 2, 2, 2]
        self.widths = [5, 6, 15, 5, 5, 5]
        self.head_flag = False
        print("got here")
        self.slot_frame_list = []
        self.add_new()
        self.add_button()

    def add_head(self):
        self.pack(fill=BOTH, expand=True)

        # Add timer frame
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text=" # ", width=self.widths[0])
        lbl1.pack(side=LEFT, padx=self.padxs[0], pady=self.pady)

        lbl2 = Label(frame1, text=" Status ", width=self.widths[1])
        lbl2.pack(side=LEFT, padx=self.padxs[1], pady=self.pady)

        lbl3 = Label(frame1, text=" Time ", width=self.widths[2])
        lbl3.pack(side=LEFT, padx=self.padxs[2], pady=self.pady)

        lbl4 = Label(frame1, text=" Start/Stop ", width=self.widths[3])
        lbl4.pack(side=LEFT, padx=self.padxs[3], pady=self.pady)

        lbl5 = Label(frame1, text=" Reset ", width=self.widths[4])
        lbl5.pack(side=LEFT, padx=self.padxs[4], pady=self.pady)

    def add_new(self):
        self.slot_count += 1
        self.construct_new_slote()


    def construct_new_slote(self):
        self.pack(fill=BOTH, expand=True)
        if not self.head_flag:
            self.add_head()
            self.head_flag = True

        # Add timer frame
        frame_slot = Frame(self)
        frame_slot.pack(fill=X)

        self.slot_frame_list.append(frame_slot)

        lbl1 = Label(frame_slot, text="{}".format(self.slot_count), width=self.widths[0])
        lbl1.pack(side=LEFT, padx=self.padxs[0], pady=self.pady)

        lbl2 = Label(frame_slot, text="N/A".format(self.slot_count), width=self.widths[1])
        lbl2.pack(side=LEFT, padx=self.padxs[1], pady=self.pady)

        self.entry_time = Entry(frame_slot, width=self.widths[2])
        self.entry_time.pack(side=LEFT, padx=self.padxs[2], pady=self.pady)

        btn_start_timer = tk.Button(frame_slot, text='Start', fg='red', width=self.widths[3], command=self.timer_clicked) # start/stop
        btn_start_timer.pack(padx=self.padxs[3], pady=self.pady, side=tk.LEFT)

        btn_reset_timer = tk.Button(frame_slot, text='Reset', fg='red', width=self.widths[4], command=self.timer_clicked) # reset
        btn_reset_timer.pack(padx=self.padxs[4], pady=self.pady, side=tk.LEFT)

        btn_remove_timer = tk.Button(frame_slot, text='Remove', fg='red', width=self.widths[5],
                                    # command=self.remove_slot
                                     )  # reset
        # btn_remove_timer['command']=self.remove_slot
        btn_remove_timer['command'] = lambda arg=frame_slot: self.remove_slot(arg) # lambda function that calls another function with argument
        btn_remove_timer.pack(padx=self.padxs[5], pady=self.pady, side=tk.LEFT)

    def remove_slot(self, reference=None):
        print("removing slot ")
        if reference is not None:
            print(reference)
            # first remove this item from list
            # print("before ", self.slot_frame_list)
            self.slot_frame_list.remove(reference)
            # print("after ", self.slot_frame_list)

            # then destroy it
            reference.destroy()
            self.slot_count -= 1 # decrease slot_count by one

        count = 1
        for frame in self.slot_frame_list:
            # get the label count and relabel it
            for child in frame.winfo_children():
                print(child['text'])
                # print(child['name'])
                print(child)
            count += 1


        pass

    def timer_clicked(self, ):
        print("button liecked")
        entered_value = self.entry_time.get()
        if "hh" in entered_value or "mm" in entered_value or "ss" in entered_value:
            print("value not valid")
            return
        if "h" in entered_value or "m" in entered_value or "s" in entered_value:
            print("time format not implemented")
            return
        decoded = self.to_seconds(entered_value)
        print(decoded, " sec")
        # sleep for specified seconds
        # create the class instance
        timer = Timer(decoded)
        timer.start()

        print("while sleeping")
        # time.sleep(2)
        # print("selpt for ", timer.peek() , " sec")

        return decoded

    def add_button(self):
        btn_reset_timer = tk.Button(self.root, text='Add New Timer', fg='red', width=10,
                                    command=self.add_new)  # reset
        btn_reset_timer.pack(padx=self.padxs[4], pady=self.pady, side=tk.BOTTOM)
        pass


def main():
    root = Tk()

    root.geometry("400x400+300+300")
    app = StopwatchSlot(root)
    # app.add_new()
    # app.add_new()
    # app.add_new()

    app.pack()
    root.mainloop()


if __name__ == '__main__':
    main()