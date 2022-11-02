import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess

login = tk.Tk()
style = ttk.Style(login)

login.configure(bg="#202020")
style.configure(
    'TLabel',
    background="#202020",
    foreground="#fafafa",
)

login.title("Login")

window_width = 700
window_height = 800
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

login.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)

sqlName = tk.StringVar()
sqlPass = tk.StringVar()
sqlDb = tk.StringVar()
username = tk.StringVar()


login_pic = tk.PhotoImage(file="achetz\login_icon.png")


heading = ttk.Label(
    login,
    font=('Poiret One', 40),
    text="Login to Enlightenment",
    image=login_pic,
    compound='top'
)

heading.pack(
    pady=50
)

nameText = ttk.Label(
    login,
    font=('Lato', 15),
    text='mySQL username: ',
)

nameText.pack(
    padx=50,
    anchor=tk.W,
)

nameEntry = tk.Entry(
    login,
    textvariable=sqlName,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

nameEntry.focus()
nameEntry.pack(
    padx=100,
    pady=10,
    fill=tk.X
)

ttk.Label(login).pack(pady=10)

passText = ttk.Label(
    login,
    font=('Lato', 15),
    text='mySQL password: ',
)

passText.pack(
    padx=50,
    anchor=tk.W,
)

passEntry = tk.Entry(
    login,
    textvariable=sqlPass,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
    show="•",
)

passEntry.pack(
    padx=100,
    pady=10,
    fill=tk.X
)

ttk.Label(login).pack(pady=10)

userText = ttk.Label(
    login,
    font=('Lato', 15),
    text='What should we call you? ',
)

userText.pack(
    padx=50,
    anchor=tk.W,
)

userEntry = tk.Entry(
    login,
    textvariable=username,
    font=('Manrope', 14),
    background="#303030",
    foreground="#fafafa",
    borderwidth=0,
)

userEntry.pack(
    padx=100,
    pady=10,
    fill=tk.X
)


def signIn():
    try:
        sqldatabase = mysql.connector.connect(
            host="localhost",
            user=sqlName.get(),
            password=sqlPass.get()
        )
        with open("credentials.txt", "w") as file:
            file.write(
                str(sqlName.get() + " -|- " +
                    sqlPass.get() + " -|- " +
                    username.get())
            )
        login.quit()
        subprocess.call('python home.py')
    except:
        subprocess.call('python popups/connect_error.py')
        sqlName.set("")
        sqlPass.set("")


submit = tk.Button(
    login,
    text="Log in",
    font=('Manrope Bold', 15),
    background="#303030",
    foreground="#eaeaea",
    command=signIn,
    cursor='dot',
    height=2,
    width=10,
    borderwidth=0,
    activebackground="#404040",
    activeforeground="#eaeaea"
)

submit.pack(
    pady=10
)

login.mainloop()
