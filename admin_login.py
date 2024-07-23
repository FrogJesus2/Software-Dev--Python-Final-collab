from tkinter import *
from tkinter import messagebox
import sqlite3
import os

class Admin:

    #This function defines the tkinter window alongside its labels and buttons
    def __init__(self,root):
        self.root = root
        self.root.geometry("245x120")

        self.myLabel = Label(root, text="Username: ")
        self.myLabel.place(relx= 0.25, rely = 0.25, anchor = CENTER)

        self.myLabel2 = Label(root, text="Password: ")
        self.myLabel2.place(relx= 0.25, rely = 0.45, anchor = CENTER)

        self.myLabel3 = Label(root, text="Admin login")
        self.myLabel3.pack()

        self.username = Entry(root)
        self.username.place(relx= 0.62, rely = 0.25, anchor = CENTER)

        self.password = Entry(root, show='*')
        self.password.place(relx= 0.62, rely = 0.45, anchor = CENTER)

        self.login = Button(root, text="Login", command=self.admin_login)
        self.login.place(relx=0.5, rely=0.65, anchor=CENTER)

    # Displays a message box when the admin_login function is called and returns with incorrect info
    def message_box(self):
        messagebox.showinfo("Try again.", "Invalid login credentials, please try again")

    def admin_login(self):
        # Have to connect to database and create cursor object
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        # Checks and gets the username and password entered from the entry labels
        username_entered = self.username.get()
        password_entered = self.password.get()

        # Fetches the query from the admin table that has admin credentials and checks it by username_entered and password_entered
        cursor.execute("SELECT * FROM admin WHERE admin_user=? and admin_password=?", (username_entered, password_entered))
        outcome = cursor.fetchone()

        # The reason we imported the os module so we can successfully close the login screen upon successful login and open the main application
        if outcome:
            self.root.after(500, lambda: os.system('python main.py'))
            self.root.after(500, self.root.destroy)
        # The message box we defined earlier displays upon failed login
        else:
            self.message_box()
        # Close the connection to end database usage properly
        conn.close()


if __name__ == "__main__":
    root = Tk()
    app = Admin(root)
    root.mainloop()