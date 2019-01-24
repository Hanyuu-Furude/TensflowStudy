import tkinter as tk
from tkinter import messagebox


def hi():
    tk.messagebox._show("Hanyuu", "Hanyuu message")


top = tk.Tk()
top.title('Hanyuu Form')
top.geometry('300x400')  # 设置大小

lebel = tk.Label(top, text="Hanyuu Label")
lebel.pack(side=tk.RIGHT)

li = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.']
lis = tk.Listbox(top)
for x in li:
    lis.insert(0, x)
lis.pack(side=tk.LEFT)

btn = tk.Button(top, text="Inari", command=hi)
btn.text = "Hanyuu"
btn.pack(side=tk.BOTTOM)
btnquit = tk.Button(top, text='quit', command=quit)
btnquit.pack(before=btn, side=tk.BOTTOM)

# menu = tk.Menu(top)
# menu.pack(tk.TOP)
type(dir(tk.messagebox))

try:
    top.mainloop()  # 消息循环
except:
    pass
