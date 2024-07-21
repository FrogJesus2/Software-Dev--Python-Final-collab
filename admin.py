from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root = Tk()
# Setting the size of the tkinter login screen
root.geometry("245x120")

# Message box for if you fail to login
def message_box():
    messagebox.showinfo("Try again.", "Invalid login credentials, please try again")

# The admin login process
def admin_login():
    # Have to connect to database and create cursor object
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Checks and gets the username and password entered from the entry labels
    username_entered = username.get()
    password_entered = password.get()

    # Fetches the query from the admin table that has admin credentials and checks it by username_entered and password_entered
    cursor.execute("SELECT * FROM admin WHERE admin_user=? and admin_password=?", (username_entered, password_entered))
    outcome = cursor.fetchone()

    # The reason we imported the os module so we can successfully close the login screen upon successful login and open the main application
    if outcome:
        root.after(500, lambda: os.system('python main.py'))
        root.after(500, root.destroy)
    # The message box we defined earlier displays upon failed login
    else:
        message_box()
    # Close the connection to end database usage properly
    conn.close()

myLabel = Label(root, text="Username: ")
myLabel.place(relx= 0.25, rely = 0.25, anchor = CENTER)

myLabel2 = Label(root, text="Password: ")
myLabel2.place(relx= 0.25, rely = 0.45, anchor = CENTER)

myLabel3 = Label(root, text="Admin login")
myLabel3.pack()

username = Entry(root)
username.place(relx= 0.62, rely = 0.25, anchor = CENTER)

password = Entry(root, show='*')
password.place(relx= 0.62, rely = 0.45, anchor = CENTER)

login = Button(root, text="Login", command=admin_login)
login.place(relx=0.5, rely=0.65, anchor=CENTER)

root.mainloop()
