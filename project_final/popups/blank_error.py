import tkinter as tk
from tkinter import ttk

blankError = tk.Tk()

style = ttk.Style(blankError)

blankError.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

iiix = "100"

blankError.title("Error")

window_width = 500
window_height = 300
screen_width = blankError.winfo_screenwidth()
screen_height = blankError.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

blankError.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\error_icon.png")

warningText = tk.Label(
    blankError,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="You've left one or more fields blank.\n Please check your inputs again.",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    blankError,
    text="Okay",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: blankError.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

blankError.mainloop()
