
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry, Button
import tkinter as tk
import time
from threading import Timer
import threading


class Converters:

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



class StopwatchTab(Frame, Converters):

    def __init__(self, args):
        super().__init__(args)
        self.construct()

    def construct(self):

        self.pack(fill=BOTH, expand=True)

        # Add timer frame
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter Time", width=10)
        lbl1.pack(side=LEFT, padx=10, pady=5)

        self.entry_time = Entry(frame1)
        self.entry_time.pack(side=LEFT, padx=20, pady=5)

        btn_add_timer = tk.Button(frame1, text='Add Timer', fg='red', command=self.timer_clicked)
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

class ClockTab():
    pass


class AlarmTab():
    pass




CONFIG={
    "background":"#4D4D4D"
}
class RootWindow(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("400x400+300+300")
        self.title("PyAlarm")
        self.minsize(640, 400)
        # self.maxsize(640, 400)
        self.configure(background=CONFIG['background'])


        tabControl = tk.ttk.Notebook(self)
        tab_clock = Frame(tabControl)
        tabControl.add(tab_clock, text='Clock')

        tab_alarm = Frame(tabControl)
        tabControl.add(tab_alarm, text='Alarm')


# testing area
        tab_example = StopwatchTab(tabControl)
        tabControl.add(tab_example, text='Stopwatch')

        tabControl.pack(expan=1, fill=BOTH)

def main():
    root = RootWindow()
    root.mainloop()

def test():
    run = input("sec > ")
    # Loop until we reach 20 minutes running
    print("looping for ", int(run), " sec")
    step=2
    sec = 0
    while sec < int(run):
        print(">>>>>>>>>>>>>>>>>>>>> {}".format(sec))
        # Sleep for a minute
        time.sleep(step)
        # Increment the minute total
        sec += step
        # Bring up the dialog box here

def test2():

    run = int(input("sec > "))

    def timeout(foo, bar=None):
        print("Thread id ", threading.currentThread().ident)
        print('The arguments were: foo: {}, bar: {}'.format(foo, bar))

    # duration is in seconds
    t = Timer(run, timeout, args=['something'], kwargs={'bar': 'else'})
    print("Thread id ", threading.currentThread().ident)
    t.start()
    print("Thread id ", threading.currentThread().ident)
    # t.join()

if __name__ == '__main__':
    print("Thread id ", threading.currentThread().ident)
    # main()
    # test()
    test2()
    # test2()
