import tkinter as tk
from  time import strftime
    


root=tk.Tk()
root.title("disital clock")
root.resizable(False,False)



def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)

label=tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack()

update_time()





root.mainloop()