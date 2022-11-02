import tkinter as tk
from tkinter import ttk

existsError = tk.Tk()

style = ttk.Style(existsError)

existsError.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

iiix = "100"

existsError.title("Error")

window_width = 500
window_height = 300
screen_width = existsError.winfo_screenwidth()
screen_height = existsError.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

existsError.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\exists_icon.png")

warningText = tk.Label(
    existsError,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="The book which you tried to add already exists.\n Please add a different book.",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    existsError,
    text="Okay",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: existsError.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

existsError.mainloop()
