import tkinter as tk
from tkinter import ttk

mailError = tk.Tk()

style = ttk.Style(mailError)

mailError.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

iiix = "100"

mailError.title("Error")

window_width = 500
window_height = 300
screen_width = mailError.winfo_screenwidth()
screen_height = mailError.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

mailError.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\email_icon.png")

warningText = tk.Label(
    mailError,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="This software supports only Gmail.\n Please enter a Gmail ID.",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    mailError,
    text="Okay",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: mailError.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

mailError.mainloop()
