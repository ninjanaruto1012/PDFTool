import os
from tkinter import *
from tkinter import filedialog

def openfile():
    filename = filedialog.askopenfilenames(parent=root, initialdir="C:\\Users\\Tri Nguyen\\Documents", title="Select File")
    print(filename)

root = Tk()
root.geometry("300x300")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()