import tkinter as tk
import tkinter.messagebox

countA = 0
countA = int()


def handler(event, x):
    print(event)


def handlerAdaptor(fun, **kwds):
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


def hi():
    label['text'] = 'Hanyuu modified label'
    tk.messagebox._show("Hanyuu", "Hanyuu message")
    btn['text'] = 'Push me'


top = tk.Tk()
top.title('Hanyuu Form')
top.geometry('300x400')  # 设置大小

label = tk.Label(top, text="Hanyuu Label")
label['bg'] = 'black'
label['fg'] = 'blue'
label['font'] = 'Consolas', 15
label.pack(side=tk.TOP)


li = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.']
lis = tk.Listbox(top)
for x in li:
    lis.insert(0, x)
lis.pack(side=tk.TOP)

stringvar = tk.StringVar()
# stringvar = 'Hanyuu'
btn = tk.Button(top, text='Hanyuu')
btn.bind('<Button-1>', handlerAdaptor(handler, x=1))
btn.pack(side=tk.BOTTOM, anchor='n', fill='both')
btnquit = tk.Button(top, text='quit', command=quit)
btnquit.pack(before=btn, side=tk.BOTTOM, anchor='n', fill=tk.BOTH)

# tk._test()
try:
    top.mainloop()  # 消息循环
except:
    pass
