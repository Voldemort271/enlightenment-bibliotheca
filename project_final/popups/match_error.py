import tkinter as tk
from tkinter import ttk

matchError = tk.Tk()

style = ttk.Style(matchError)

matchError.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

iiix = "100"

matchError.title("Error")

window_width = 500
window_height = 300
screen_width = matchError.winfo_screenwidth()
screen_height = matchError.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

matchError.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\match_icon.png")

warningText = tk.Label(
    matchError,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="Our records don't match with your email ID.\n Please check your inputs.",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    matchError,
    text="Okay",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: matchError.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

matchError.mainloop()
