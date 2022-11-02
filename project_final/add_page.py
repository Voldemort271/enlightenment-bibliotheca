import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess

details = {}
with open("credentials.txt") as file:
    lis = file.read().split(" -|- ")
    details['username'] = lis[0]
    details['password'] = lis[1]
    details['nickname'] = lis[2]


sqldatabase = mysql.connector.connect(
    host="localhost",
    user=details['username'],
    password=details['password'],
    database="lib"
)
sqlcursor = sqldatabase.cursor()
add = tk.Tk()
style = ttk.Style(add)

add.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

add.title("Add Books")

window_width = 1000
window_height = 800
screen_width = add.winfo_screenwidth()
screen_height = add.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

add.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)


add_pic = tk.PhotoImage(file=r"achetz\add_book.png")

heading = ttk.Label(
    add,
    font=('Poiret One', 40),
    text="Add Books to Enlightenment",
    image=add_pic,
    compound='top',
)

heading.pack(
    pady=30
)

sqlcursor.execute("select * from all_books order by id")

books = []
for i in sqlcursor:
    books += [i]
latest = books[-1][0]

bookName = tk.StringVar()
authorName = tk.StringVar()

ttk.Label(add).pack(pady=20)

nameText = ttk.Label(
    add,
    text='Name of book: ',
    font=('Lato', 15),
)

nameText.pack(
    padx=100,
    pady=10,
    anchor=tk.W
)

nameEntry = tk.Entry(
    add,
    textvariable=bookName,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

nameEntry.focus()
nameEntry.pack(
    padx=100,
    fill=tk.X
)

ttk.Label(add).pack(pady=10)

authorText = ttk.Label(
    add,
    text='Name of author: ',
    font=('Lato', 15),
)

authorText.pack(
    padx=100,
    pady=10,
    anchor=tk.W
)

authorEntry = tk.Entry(
    add,
    textvariable=authorName,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

authorEntry.pack(
    padx=100,
    fill=tk.X
)


def confirmAdd():
    global latest

    sqlcursor.execute("select * from all_books order by id")
    booknames = []
    for i in sqlcursor:
        booknames += [i[1]]

    if authorName.get() == "" or bookName.get() == "":
        subprocess.call('python popups/blank_error.py')
        bookName.set("")
        authorName.set("")

    elif bookName.get() in booknames:
        subprocess.call('python popups/exists_error.py')
        bookName.set("")
        authorName.set("")

    else:
        subprocess.call('python popups/added_info.py')

        sqlcursor.execute(
            f"insert into all_books values ({latest + 1}, '{bookName.get()}', '{authorName.get()}')"
        )
        sqldatabase.commit()

        sqlcursor.execute(
            f"insert into available_books values ({latest + 1}, '{bookName.get()}', '{authorName.get()}')"
        )
        sqldatabase.commit()

        latest = books[-1][0]
        bookName.set("")
        authorName.set("")





submit = tk.Button(
    add,
    text="Add Book",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=confirmAdd,
    cursor='dot',
    height=2,
    width=10,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.pack(
    pady=50
)

add.mainloop()
