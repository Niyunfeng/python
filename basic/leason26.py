#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Trinker

import tkinter as tk
from tkinter import messagebox

hit_status = False


def B_Callback():
    # global hit_status
    # messagebox.showinfo(" ", "running")
    # if hit_status == False:
    #     var.set("Hello python")
    #     hit_status = True
    # else:
    #     var.set("")
    #     hit_status = False
    value = lb.get(lb.curselection())
    var.set(value)


def print_selection():
    lr.config(text="you have selected " + var3.get())


def insert_point():
    var = e.get()
    t.insert("insert", var)


def insert_end():
    var = e.get(lb.curselection())
    t.insert("end", var)


window = tk.Tk()
window.title("Tkinter")
window.geometry("720x480")
var = tk.StringVar()
var2 = tk.StringVar()
var2 = set((11, 22, 33, 44))
var3 = tk.StringVar()
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert("end", item)
lb.insert(1, "first")
lb.insert(2, "second")
lb.delete(2)
lb.pack()
e = tk.Entry(window, show="*")
e.pack()
t = tk.Text(window, height=2)
t.pack()
l = tk.Label(window, bg="yellow", width=4, textvariable=var)
l.pack()
r1 = tk.Radiobutton(
    window, text="Option A", variable=var3, value="A", command=print_selection
)
r1.pack()
r2 = tk.Radiobutton(
    window, text="Option B", variable=var3, value="B", command=print_selection
)
r2.pack()
r3 = tk.Radiobutton(
    window, text="Option C", variable=var3, value="C", command=print_selection
)
r3.pack()
b = tk.Button(
    window,
    text="Button",
    width=12,
    height=2,
    activeforeground="blue",
    command=B_Callback,
)
b.pack()
b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end", command=insert_end)
b2.pack()

lr = tk.Label(window, text="empty", width=20, bg="blue")
lr.pack()

window.mainloop()

