import tkinter as tk

height, width = 350,250
root = tk.Tk() 
root.minsize(width, height)

frame = tk.Frame(root) 
frame.pack() 

time_label = tk.Label(frame, text='Enter Time').pack(side=tk.LEFT)
e1 = tk.Entry(frame).pack()
# e1.grid(row=0, column=1) 


# bottomframe = tk.Frame(root) 
# bottomframe.pack( side = tk.BOTTOM ) 
redbutton = tk.Button(frame, text = 'Add Timer', fg ='red') 
redbutton.pack( side = tk.RIGHT) 


root.mainloop() 