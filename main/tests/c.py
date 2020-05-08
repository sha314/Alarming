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




root.mainloop() 