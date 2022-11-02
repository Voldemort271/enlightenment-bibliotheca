import tkinter as tk
from tkinter import ttk

readError = tk.Tk()

style = ttk.Style(readError)

readError.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

iiix = "100"

readError.title("Error")

window_width = 600
window_height = 300
screen_width = readError.winfo_screenwidth()
screen_height = readError.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

readError.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\read_icon.png")

warningText = tk.Label(
    readError,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="You're expected to read the book once you take it.\n Please return only after reading.",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    readError,
    text="Okay",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: readError.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

readError.mainloop()
