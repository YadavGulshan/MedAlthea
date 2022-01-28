from tkinter import *

root = Tk()
name = Entry(root,bg="white", width=50, borderwidth=5).grid(row=0, column=0)


def printIt():
    print(name)


Button(root, text="click", padx=10, pady=10, command=printIt).grid(row=1, column=0)
root.mainloop()
