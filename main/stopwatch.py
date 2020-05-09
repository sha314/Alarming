from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
import tkinter as tk
from PIL import Image, ImageTk
import os
import threading
import time

# local
# import main.iconbox as iconbox
import iconbox
import converters



class StopwatchSlot:
    def __init__(self, root):
        self.root = root
        # super(StopwatchSlot, self).__init__(root)
        self.slot_count=0
        self.slot_frame_list = []
        self.pady = 2
        self.padxs = [1, 2, 15, 2, 2, 2]
        self.widths = [5, 6, 15, 5, 5, 5]
        self.height = 1
        self.slots = []
        self.construct()
        self.add_new_slot()
        pass

    def construct(self):
        self.btn_add_new_slot = tk.Button(self.root, text="New", command=self.add_new_slot)
        self.btn_add_new_slot.pack(side=tk.BOTTOM)

    def add_new_slot(self):
        self.slot_count += 1
        self.slots.append(Slot(self.root, self.slot_count))


class Slot:
    """
    One slot only.
    then Stopwatch class will create instances of this to create multiple Slot objects
    """
    def __init__(self, master, id=0):
        self.master = master
        self.slot_id = id
        # super().__init__(master)
        # photo = tk.PhotoImage(file=r"../resources/icon/png/delete.png")
        # self.icon = photo.subsample(2, 2)  # Resizing image to fit on button
        self.padxs = [1, 2, 15, 2, 2, 2]
        self.widths = [5, 8, 15, 5, 5, 5]
        self.height = 1
        self.pady=1
        self.is_running = False  # false means not running
        self.icons = iconbox.IconBox().get_all(25, 25)
        self.duration = tk.StringVar()
        self.construct()

    def construct(self):
        # self.pack(fill=BOTH, expand=True)
        # if not self.head_flag:
        #     self.add_head()
        #     self.head_flag = True

        # Add timer frame
        self.frame_slot = Frame(self.master)

        self.lbl_id = Label(self.frame_slot, text="{}".format(self.slot_id).format(self.slot_id), width=self.widths[0])
        self.lbl_status = Label(self.frame_slot, text="N/A".format(self.slot_id), width=self.widths[1])
        self.entry_time = Entry(self.frame_slot, width=self.widths[2], textvariable=self.duration)
        self.duration.set("00:00:00")
        self.btn_start_timer = tk.Button(self.frame_slot,)  # start/stop
        self.btn_reset_timer = tk.Button(self.frame_slot, )  # reset
        self.btn_remove_timer = tk.Button(self.frame_slot,)  # reset

        ## commands
        # self.btn_remove_timer['command'] = lambda arg=frame_slot: self.clicked_btn_delete(
        #     arg)  # lambda function that calls another function with argument
        self.btn_start_timer['command'] = self.clicked_btn_start
        self.btn_reset_timer['command'] = self.clicked_btn_reset
        self.btn_remove_timer['command'] = self.clicked_btn_delete

        ## icon
        self.btn_start_timer['image'] = self.icons['start']
        # btn_reset_timer['image'] = self.icons['reset']
        self.btn_reset_timer['image'] = self.icons['reset']
        self.btn_remove_timer['image'] = self.icons['delete']


        ## packing
        self.lbl_id.pack(side=LEFT, padx=self.padxs[0], pady=self.pady)
        self.lbl_status.pack(side=LEFT, padx=self.padxs[1], pady=self.pady)
        self.entry_time.pack(side=LEFT, padx=self.padxs[2], pady=self.pady)
        self.btn_start_timer.pack(padx=self.padxs[3], pady=self.pady, side=tk.LEFT)
        self.btn_reset_timer.pack(padx=self.padxs[4], pady=self.pady, side=tk.LEFT)
        self.btn_remove_timer.pack(padx=self.padxs[5], pady=self.pady, side=tk.LEFT)
        self.frame_slot.pack(fill=X)

        pass

    def set_id(self, id):
        self.slot_id = id
        self.lbl_id['text'] = "{}".format(id)

    def clicked_btn_start(self):
        if not self.is_running:
            self.btn_start_timer['image'] = self.icons['stop']
            self.lbl_status['text'] = "Running"
            self.is_running = True

            print("Current Thread ", threading.currentThread().ident)
            self.seconds_to_sleep = converters.to_seconds(self.duration.get())
            th = threading.Thread(target=self.run_timer)
            th.start()

        else:
            self.btn_start_timer['image'] = self.icons['start']
            self.lbl_status['text'] = "Stopped"
            self.is_running = False

            pass

        print(self.duration.get())
        print(self.seconds_to_sleep, ' sec to sleep')
        print("convert to second and start timer")
        pass

    def run_timer(self):
        print("running timer ", threading.currentThread().ident)
        strs = converters.seconds_to_hhmmss(self.seconds_to_sleep)
        self.duration.set(strs)
        seconds_to_sleep = self.seconds_to_sleep
        while seconds_to_sleep > 0:
            if not self.is_running:
                break
            time.sleep(1)
            seconds_to_sleep -= 1
            strs = converters.seconds_to_hhmmss(seconds_to_sleep)
            self.duration.set(strs)
            pass
        print("Complete running")
        self.stop_clock()

    def stop_clock(self):
        print("clicked_btn_stop")
        # self.timer.join()
        self.lbl_status['text'] = "Time Up"
        self.duration.set("00:00:00")
        self.btn_start_timer['image'] = self.icons['start']
        self.lbl_status['text'] = "Stopped"
        self.is_running = False
        pass

    def clicked_btn_reset(self):
        self.stop_clock()
        self.lbl_status['text'] = "Ready"
        print(self.duration.get())
        strs = converters.seconds_to_hhmmss(self.seconds_to_sleep)
        self.duration.set(strs)

        pass

    def clicked_btn_delete(self, reference=None):
        self.stop_clock()
        print("clicked_btn_delete")
        self.frame_slot.destroy()
        # if reference is not None:
        #     print(reference)
        #     # first remove this item from list
        #     # print("before ", self.slot_frame_list)
        #     # self.slot_frame_list.remove(reference)
        #     # print("after ", self.slot_frame_list)
        #
        #     # then destroy it
        #     reference.destroy()


        # count = 1
        # for frame in self.slot_frame_list:
        #     # get the label count and relabel it
        #     for child in frame.winfo_children():
        #         print(child['text'])
        #         # print(child['name'])
        #         print(child)
        #     count += 1

        pass


def main():
    root = Tk()

    root.geometry("400x400+300+300")
    # root.iconbitmap('../resources/png/icon.ico') # main icon
    # root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png')) # or this

    app = StopwatchSlot(root)
    # app = Slot(root)
    # app.add_new()
    # app.add_new()
    # app.add_new()

    # app.pack()
    root.mainloop()


if __name__ == '__main__':
    main()

    pass