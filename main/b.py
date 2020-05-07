import tkinter as tk

# input format hhmmss
# example 2h3m5s
def decode_to_hms(s):
	"""
	Decode string to hour minute second
	"""
	s = s.replace(" ", "")
	a = s.split('h')
	hr=a[0]
	b = a[1].split('m')
	mn=b[0]
	sec=b[1].split('s')[0]
	print(s)
	return hr,mn,sec

def timer_clicked():
	print("button liecked")
	entered_value = entry_time.get()
	decoded = decode_to_hms(entered_value)
	print(decoded)
	pass

height, width = 350,250
root = tk.Tk() 
root.minsize(width, height)


frame = tk.Frame(root) 
frame.pack() 

label_time = tk.Label(frame, text='Enter Time')
label_time.pack(padx=5, pady=10, side=tk.LEFT)
entry_time = tk.Entry(frame)
entry_time.pack(padx=10, pady=20, side=tk.LEFT)
btn_add_timer = tk.Button(frame, text = 'Add Timer', fg ='red', command=timer_clicked) 
btn_add_timer.pack(padx=5, pady=20, side=tk.LEFT)




root.mainloop() 