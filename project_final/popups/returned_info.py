import tkinter as tk
from tkinter import ttk

returnedInfo = tk.Tk()

style = ttk.Style(returnedInfo)

returnedInfo.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

returnedInfo.title("Done")

window_width = 500
window_height = 300
screen_width = returnedInfo.winfo_screenwidth()
screen_height = returnedInfo.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

returnedInfo.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}')

im = tk.PhotoImage(file=r"achetz\returned_book.png")

warningText = tk.Label(
    returnedInfo,
    background="#202020",
    foreground="#eaeaea",
    font=('Manrope', 15),
    text="Book returned successfully.\n Have fun!",
    image=im,
    compound='top'
)

warningText.pack(
    pady=50,
)

okButton = tk.Button(
    returnedInfo,
    text="Yayyy",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=lambda: returnedInfo.quit(),
    height=1,
    width=10,
    cursor='dot',
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

okButton.pack()

returnedInfo.mainloop()
