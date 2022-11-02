import tkinter as tk
from tkinter import ttk

loginError = tk.Tk()

style = ttk.Style(loginError)

loginError.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

loginError.title("Error")

window_width = 500
window_height = 300
screen_width = loginError.winfo_screenwidth()
screen_height = loginError.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

loginError.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\server_icon.png")

warningText = tk.Label(
    loginError,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="Server connectivity could not be established.\n Please check your credentials again.",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    loginError,
    text="Okay",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: loginError.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

loginError.mainloop()
