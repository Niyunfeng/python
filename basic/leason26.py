#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Trinker

import tkinter as tk
from tkinter import messagebox

hit_status = False


def B_Callback():
    global hit_status
    messagebox.showinfo(" ", "running")
    if hit_status == False:
        var.set("Hello python")
        hit_status = True
    else:
        var.set("")
        hit_status = False


def insert_point():
    var = e.get()
    t.insert("insert", var)


def insert_end():
    var = e.get()
    t.insert("end", var)


window = tk.Tk()
window.title("Tkinter")
window.geometry("480x480")
var = tk.StringVar()
e = tk.Entry(window, show="*")
e.pack()
t = tk.Text(window, height=2)
t.pack()
l = tk.Label(window, textvariable=var, font=("Arial", 12), width=12, height=2)
l.pack()
b = tk.Button(
    window,
    text="Button",
    width=12,
    height=2,
    activeforeground="blue",
    state="active",
    command=B_Callback,
)
b.pack()
b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text="insert end", command=insert_end)
b2.pack()

window.mainloop()

