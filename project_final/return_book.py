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


returnBook = tk.Tk()
style = ttk.Style(returnBook)

returnBook.columnconfigure(0, weight=1)
returnBook.columnconfigure(1, weight=1)

returnBook.configure(bg="#202020")

style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

style.configure(
    "TMenubutton",
    background="#303030",
    foreground="#dadada",
    font=('Manrope', 14),
)

style.configure(
    'TRadiobutton',
    font=('Manrope', 14),
    background='#202020',
    foreground='#fafafa',
)


returnBook.title("Return Books")

window_width = 1000
window_height = 800
screen_width = returnBook.winfo_screenwidth()
screen_height = returnBook.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

returnBook.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)

return_pic = tk.PhotoImage(file=r"achetz\return_icon.png")

heading = ttk.Label(
    returnBook,
    font=('Poiret One', 40),
    text="Return Book to Enlightenment",
    image=return_pic,
    compound='top',
)

heading.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)

ttk.Label(returnBook).grid(pady=10, row=2, column=0, columnspan=2)

issueHeading = ttk.Label(
    returnBook,
    text='Which book do you want to return?',
    font=('Lato', 15),
)

issueHeading.grid(
    padx=100,
    pady=10,
    row=3,
    column=0,
    sticky=tk.W
)


sqlcursor.execute("select * from issued_books order by id")

books = ["Select any one..."]

for i in sqlcursor:
    books += [f"{i[0]}. {i[1]} by {i[2]}"]

returningBook = tk.StringVar()

selectBook = ttk.OptionMenu(
    returnBook,
    returningBook,
    *books
)

selectBook["menu"].configure(
    font=('Manrope', 12),
    background="#303030",
    foreground="#fafafa",

)

selectBook.grid(
    row=4,
    column=0,
    columnspan=2,
    padx=100,
    sticky=tk.W
)

ttk.Label(returnBook, background='#202020').grid(pady=5, row=5, column=0)


readHeading = ttk.Label(
    returnBook,
    text='Have you read the book completely?',
    font=('Lato', 15),
    background='#202020',
    foreground='#fafafa'
)

readHeading.grid(
    padx=100,
    pady=10,
    row=6,
    column=0,
    sticky=tk.W
)

hasRead = tk.StringVar()

r1 = ttk.Radiobutton(
    returnBook,
    text='Yes',
    value=True,
    variable=hasRead
)

r2 = ttk.Radiobutton(
    returnBook,
    text='No',
    value=False,
    variable=hasRead
)

r1.grid(
    padx=100,
    row=7,
    column=0,
    sticky=tk.W
)

r2.grid(
    padx=100,
    row=8,
    column=0,
    sticky=tk.W
)

emailHeading = ttk.Label(
    returnBook,
    text='What is your email?',
    font=('Lato', 15),
)

emailHeading.grid(
    padx=100,
    pady=10,
    row=6,
    column=1,
    sticky=tk.W
)

emailId = tk.StringVar()

emailEntry = tk.Entry(
    returnBook,
    textvariable=emailId,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

emailEntry.focus()
emailEntry.grid(
    padx=100,
    row=7,
    column=1,
    sticky=tk.W
)

ttk.Label(returnBook).grid(pady=30, row=9, column=0, columnspan=2)


def confirmReturn():
    returningBookId = returningBook.get().split('.')[0]

    sqlcursor.execute("select * from issued_books order by id")
    emailList = []
    for i in sqlcursor:
        emailList += [i[-1]]

    if returningBook.get() == "Select your book..." or emailId.get() == "":
        subprocess.call('python popups/blank_error.py')

    elif not int(hasRead.get()):
        subprocess.call('python popups/read_error.py')

    elif emailId.get() not in emailList:
        subprocess.call('python popups/match_error.py')

    else:
        subprocess.call('python popups/returned_info.py')

        sqlcursor.execute(
            f"select * from issued_books where id = {returningBookId}")

        returnedBook = []
        for i in sqlcursor:
            returnedBook = i

        sqlcursor.execute(
            f"delete from issued_books where id = {returningBookId}")
        sqldatabase.commit()

        sqlcursor.execute(
            f"insert into available_books values {returnedBook[0:3]}")
        sqldatabase.commit()

        sqlcursor.execute("select * from issued_books order by id")

        books = ["Select your book..."]
        for i in sqlcursor:
            books += [f"{i[0]}. {i[1]} by {i[2]}"]
        
        returningBook.set('Select any one...')
        hasRead.set('')
        emailId.set('')


submit = tk.Button(
    returnBook,
    text="Return Book",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=confirmReturn,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.grid(
    row=10,
    column=0,
    columnspan=2
)

returnBook.mainloop()
