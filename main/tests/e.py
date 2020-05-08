

''' threading_count_seconds1.py
count seconds needed to complete a task
counter runs in the background
tested with Python27 and Python33  by  vegaseat  19sep2014
'''
import threading
import time
import sys
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

class Timer_gui:


    pass




class TimerLine(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/100 of a second
    '''
    def __init__(self, frame, duration=2, interval=0.01):
        # init the thread
        threading.Thread.__init__(self)
        self.duration = duration  # seconds
        self.interval = interval
        # initial value
        self.elapsed = 0
        # controls the while loop in method run
        self.alive = False

        frame.pack() 

        v = tk.StringVar(root, value='hh:mm:ss')


        label_time = tk.Label(frame, text='No')
        label_time.pack(padx=5, pady=10, side=tk.LEFT)

        label_time = tk.Label(frame, text='Time')
        label_time.pack(padx=5, pady=10, side=tk.LEFT)

        label_time = tk.Label(frame, text='ETA')
        label_time.pack(padx=5, pady=10, side=tk.LEFT)

        btn_play_pause_timer = tk.Button(frame, text = 'start', fg ='red', command=timer_clicked) 
        btn_play_pause_timer.pack(padx=5, pady=20, side=tk.LEFT)

    def run(self):
        '''
        this will run in its own thread via self.start()
        '''

        self.alive = True
        print("going to sleep mode")
        while self.elapsed < self.duration:
            time.sleep(self.interval)
            self.elapsed += self.interval
            pass
        print("waking up")
        self.alive = False
        pass


    def peek(self):
        '''
        return the current value
        '''
        return self.elapsed

    def finish_early(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.elapsed
        pass

    def btn_play_pause_timer_clicked(self):

        pass



class Timer(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/100 of a second
    '''
    def __init__(self, duration=2, interval=0.01):
        # init the thread
        threading.Thread.__init__(self)
        self.duration = duration  # seconds
        self.interval = interval
        # initial value
        self.elapsed = 0
        # controls the while loop in method run
        self.alive = False

    def run(self):
        '''
        this will run in its own thread via self.start()
        '''

        self.alive = True
        print("going to sleep mode")
        while self.elapsed < self.duration:
            time.sleep(self.interval)
            self.elapsed += self.interval
            pass
        print("waking up")
        self.alive = False
        pass


    def peek(self):
        '''
        return the current value
        '''
        return self.elapsed

    def finish_early(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.elapsed
        pass
    pass


def main():
    print("to be implemented")
    pass

height, width = 350,250
root = tk.Tk() 
root.minsize(width, height)


frame = tk.Frame(root) 
frame.pack() 

v = tk.StringVar(root, value='hh:mm:ss')


label_time = tk.Label(frame, text='Enter Time')
label_time.pack(padx=5, pady=10, side=tk.LEFT)
entry_time = tk.Entry(frame,textvariable=v)
entry_time.pack(padx=10, pady=20, side=tk.LEFT)
btn_add_timer = tk.Button(frame, text = 'Add Timer', fg ='red', command=timer_clicked) 
btn_add_timer.pack(padx=5, pady=20, side=tk.LEFT)


# prepare monitor panel

monitor_frame = tk.Frame(root)

label_time = tk.Label(frame, text='No')
label_time.pack(padx=5, pady=10, side=tk.LEFT)

label_time = tk.Label(frame, text='Time')
label_time.pack(padx=5, pady=10, side=tk.LEFT)

label_time = tk.Label(frame, text='ETA')
label_time.pack(padx=5, pady=10, side=tk.LEFT)

label_time = tk.Label(frame, text='action')
label_time.pack(padx=5, pady=10, side=tk.LEFT)



timer = TimerLine(monitor_frame)
timer.start()


root.mainloop() 








# if __name__=="__main__":
#   main()


