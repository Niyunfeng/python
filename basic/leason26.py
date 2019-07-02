#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Trinker

import tkinter as tk
from tkinter import messagebox


def B_Callback():
    messagebox.showinfo(" ", "running")


window = tk.Tk()
window.title("Tkinter")
window.geometry("480x240")
l = tk.Label(window, text="This is Tkinter", font=("Arial", 12), width=12, height=2)
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

