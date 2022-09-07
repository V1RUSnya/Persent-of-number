from tkinter import *

def click():
    a = txt.get()
    b = txtt.get()
    a = int(a)
    b = int(b)
    c = a / 100 * b
    lblll.configure(text=c)

root = Tk()
root.title('Percent of number')
root.geometry('300x100')
root.wm_attributes('-alpha', 0.95)
root.resizable(width=False, height=False)

frame = Frame(root)
frame.place(relx=0.175, rely=0.15, relwidth=0.7, relheight=0.7)

lbl = Label(frame, text='Number')
lbl.grid(column=1, row=0)
lbll = Label(frame, text='Percent')
lbll.grid(column=3, row=0)
lblll = Label(frame, text='Answer')
lblll.grid(column=2, row=3)

txt = Entry(frame, width=10)
txt.grid(column=1, row=1)
txtt = Entry(frame, width=10)
txtt.grid(column=3, row=1)

btn = Button(frame, text='Calculate', command=click)
btn.grid(column=2, row=0)

root.mainloop()
