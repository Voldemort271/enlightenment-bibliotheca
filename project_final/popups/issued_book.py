import tkinter as tk
from tkinter import ttk

book = tk.Tk()
style = ttk.Style(book)

book.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

book.title("Your Book")

window_width = 600
window_height = 600
screen_width = book.winfo_screenwidth()
screen_height = book.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

book.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)

subheading = tk.Label(
    book,
    text="Thank you for shopping with us! Here's your book:",
    font=('Lato', 15),
    background='#202020',
    foreground='#fafafa'
)

subheading.pack(
    fill=tk.X,
    padx=10,
    pady=10
)

no_pic = tk.PhotoImage(file=r'achetz\display_book.png')

image = tk.Label(
    book,
    image=no_pic,
    background="#202020"
)

image.pack(
    padx=10,
    pady=10
)

book.mainloop()
