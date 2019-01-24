#!/usr/bin/python
import sys
import time
import tkinter as tk


class Logger(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack(expand=tk.YES, fill=tk.BOTH)

        self.master.title("Hanyuu's Timestamp logging application")
        self.tslist = []
        self.tsdisp = tk.Text(height=6, width=25)
        self.count = tk.StringVar()
        self.cntdisp = tk.Message(font=('Sans', 24),
                                  textvariable=self.count)
        self.log = tk.Button(text="Log Timestamp",
                             command=self.log_timestamp)
        self.quit = tk.Button(text="Quit", command=sys.exit)
        self.tsdisp.pack(side=tk.LEFT)
        self.cntdisp.pack()
        self.log.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
        self.quit.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def log_timestamp(self):
        stamp = time.ctime()
        self.tsdisp.insert(tk.END, stamp+"\n")
        self.tsdisp.see(tk.END)
        self.tslist.append(stamp)
        self.count.set("% 3d" % len(self.tslist))


if __name__ == '__main__':
    try:
        Logger().mainloop()
    except:
        quit()
