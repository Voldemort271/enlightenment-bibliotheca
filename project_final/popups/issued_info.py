import tkinter as tk
from tkinter import ttk

issuedInfo = tk.Tk()

style = ttk.Style(issuedInfo)

issuedInfo.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

issuedInfo.title("Done")

window_width = 500
window_height = 300
screen_width = issuedInfo.winfo_screenwidth()
screen_height = issuedInfo.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

issuedInfo.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\issued_icon.png")

warningText = tk.Label(
    issuedInfo,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="You own the book now.\n Have fun!",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    issuedInfo,
    text="Yayyy",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: issuedInfo.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

issuedInfo.mainloop()
