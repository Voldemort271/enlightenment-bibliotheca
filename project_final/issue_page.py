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

issue = tk.Tk()
style = ttk.Style(issue)

issue.columnconfigure(0, weight=1)
issue.columnconfigure(1, weight=1)

issue.configure(bg="#202020")
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


issue.title("Issue Books")

window_width = 1000
window_height = 800
screen_width = issue.winfo_screenwidth()
screen_height = issue.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

issue.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)


issue_pic = tk.PhotoImage(file="achetz\issue_book.png")

heading = ttk.Label(
    issue,
    font=('Poiret One', 40),
    text="Get Books from Enlightenment",
    image=issue_pic,
    compound='top',
)

heading.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)

ttk.Label(issue).grid(pady=10, row=2, column=0, columnspan=2)


issueHeading = ttk.Label(
    issue,
    text='What do you want to read?',
    font=('Lato', 15),
)

issueHeading.grid(
    padx=100,
    pady=10,
    row=3,
    column=0,
    sticky=tk.W
)


sqlcursor.execute("select * from available_books order by id")

books = ["Select any one..."]

for i in sqlcursor:
    books += [f"{i[0]}. {i[1]} by {i[2]}"]

issuingBook = tk.StringVar()

selectBook = ttk.OptionMenu(
    issue,
    issuingBook,
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
    padx=100,
    sticky=tk.W
)

ttk.Label(issue).grid(pady=5, row=5, column=0)

durationHeading = ttk.Label(
    issue,
    text='How many days do you want?',
    font=('Lato', 15)
)

durationHeading.grid(
    padx=100,
    pady=10,
    row=6,
    column=0,
    sticky=tk.W
)

duration = tk.StringVar(value=0)

durationSelect = tk.Spinbox(
    issue,
    from_=0,
    to=30,
    textvariable=duration,
    background="#303030",
    foreground="#dadada",
    font=('Manrose', 14),
    buttonbackground="#202020",
    relief=tk.FLAT,
    buttondownrelief=tk.FLAT,
    buttonuprelief=tk.FLAT,
    wrap=True
)

durationSelect.grid(
    padx=100,
    row=7,
    column=0,
    sticky=tk.W
)

nameText = ttk.Label(
    issue,
    text="What's your username?",
    font=('Lato', 15),
)

nameText.grid(
    padx=100,
    row=3,
    column=1,
    sticky=tk.W
)

username = tk.StringVar()

nameEntry = tk.Entry(
    issue,
    textvariable=username,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)
nameEntry.focus()

nameEntry.grid(
    padx=100,
    row=4,
    column=1,
    sticky=tk.W
)

username.set(details['nickname'])

tk.Label(issue, background='#202020').grid(pady=5, row=5, column=1)

mailText = ttk.Label(
    issue,
    text="What's your email?",
    font=('Lato', 15),
)

mailText.grid(
    padx=100,
    row=6,
    column=1,
    sticky=tk.W
)

emailId = tk.StringVar()

mailEntry = tk.Entry(
    issue,
    textvariable=emailId,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

mailEntry.grid(
    padx=100,
    row=7,
    column=1,
    sticky=tk.W
)


tk.Label(issue, background='#202020').grid(pady=50, row=8, column=0, columnspan=2)


def confirmIssue():
    if issuingBook.get() == "Select any one..." or int(duration.get()) == 0 or emailId.get() == "":
        subprocess.call('python popups/blank_error.py')
        issuingBook.set('Select any one...')
        duration.set('0')
        emailId.set("")

    elif "@gmail.com" not in emailId.get():
        subprocess.call('python popups/mail_error.py')
        emailId.set("")

    else:
        subprocess.call('python popups/issued_info.py')

        bookKey = issuingBook.get().split('.')[0]

        sqlcursor.execute(
            f"select * from available_books where id = {bookKey}"
        )

        for i in sqlcursor:
            sqlcursor.execute(
                f"select adddate(curdate(), interval {int(duration.get())} day)"
            )

            for j in sqlcursor:
                for dueDate in j:
                    sqlcursor.execute(
                        f"insert into issued_books values {i + (str(dueDate), emailId.get())}"
                    )
                    sqldatabase.commit()

                    sqlcursor.execute(
                        f"delete from available_books where id = {bookKey}"
                    )
                    sqldatabase.commit()

        sqlcursor.execute("select * from available_books order by id")
        books = ["Select any one..."]
        for i in sqlcursor:
            books += [f"{i[0]}. {i[1]} by {i[2]}"]

        subprocess.call('python popups/issued_book.py')



submit = tk.Button(
    issue,
    text="Issue Book",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=confirmIssue,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.grid(
    row=9,
    column=0,
    columnspan=2
)

issue.mainloop()

