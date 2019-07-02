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


window = tk.Tk()
window.title("Tkinter")
window.geometry("480x240")
var = tk.StringVar()
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


window.mainloop()

