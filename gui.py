import tkinter as tk
from tkinter import messagebox
from library import Library
from book import Book
from member import Member
from admin import Admin
from database import Database

class LibraryGUI:
    def __init__(self, root, library, admin):
        self.root = root
        self.library = library
        self.admin = admin
        self.database = Database()
        self.root.title("Library Management System")
        
        self.create_login_window()

    def create_login_window(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        self.username_label = tk.Label(self.login_frame, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.admin.authenticate(username, password):
            messagebox.showinfo("Login Success", "Welcome, Admin!")
            self.login_frame.pack_forget()
            self.create_main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def create_main_window(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        
        # Add book section
        self.add_book_frame = tk.Frame(self.main_frame)
        self.add_book_frame.pack()
        
        self.book_title_label = tk.Label(self.add_book_frame, text="Book Title")
        self.book_title_label.grid(row=0, column=0)
        self.book_title_entry = tk.Entry(self.add_book_frame)
        self.book_title_entry.grid(row=0, column=1)
        
        self.book_author_label = tk.Label(self.add_book_frame, text="Book Author")
        self.book_author_label.grid(row=1, column=0)
        self.book_author_entry = tk.Entry(self.add_book_frame)
        self.book_author_entry.grid(row=1, column=1)
        
        self.book_isbn_label = tk.Label(self.add_book_frame, text="Book ISBN")
        self.book_isbn_label.grid(row=2, column=0)
        self.book_isbn_entry = tk.Entry(self.add_book_frame)
        self.book_isbn_entry.grid(row=2, column=1)
        
        self.add_book_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=3, columnspan=2)
        
        # Add member section
        self.add_member_frame = tk.Frame(self.main_frame)
        self.add_member_frame.pack()
        
        self.member_id_label = tk.Label(self.add_member_frame, text="Member ID")
        self.member_id_label.grid(row=0, column=0)
        self.member_id_entry = tk.Entry(self.add_member_frame)
        self.member_id_entry.grid(row=0, column=1)
        
        self.member_name_label = tk.Label(self.add_member_frame, text="Member Name")
        self.member_name_label.grid(row=1, column=0)
        self.member_name_entry = tk.Entry(self.add_member_frame)
        self.member_name_entry.grid(row=1, column=1)
        
        self.add_member_button = tk.Button(self.add_member_frame, text="Add Member", command=self.add_member)
        self.add_member_button.grid(row=2, columnspan=2)
        
        # Issue book section
        self.issue_book_frame = tk.Frame(self.main_frame)
        self.issue_book_frame.pack()
        
        self.issue_isbn_label = tk.Label(self.issue_book_frame, text="Book ISBN")
        self.issue_isbn_label.grid(row=0, column=0)
        self.issue_isbn_entry = tk.Entry(self.issue_book_frame)
        self.issue_isbn_entry.grid(row=0, column=1)
        
        self.issue_member_id_label = tk.Label(self.issue_book_frame, text="Member ID")
        self.issue_member_id_label.grid(row=1, column=0)
        self.issue_member_id_entry = tk.Entry(self.issue_book_frame)
        self.issue_member_id_entry.grid(row=1, column=1)
        
        self.issue_book_button = tk.Button(self.issue_book_frame, text="Issue Book", command=self.issue_book)
        self.issue_book_button.grid(row=2, columnspan=2)
        
        # Return book section
        self.return_book_frame = tk.Frame(self.main_frame)
        self.return_book_frame.pack()
        
        self.return_isbn_label = tk.Label(self.return_book_frame, text="Book ISBN")
        self.return_isbn_label.grid(row=0, column=0)
        self.return_isbn_entry = tk.Entry(self.return_book_frame)
        self.return_isbn_entry.grid(row=0, column=1)
        
        self.return_member_id_label = tk.Label(self.return_book_frame, text="Member ID")
        self.return_member_id_label.grid(row=1, column=0)
        self.return_member_id_entry = tk.Entry(self.return_book_frame)
        self.return_member_id_entry.grid(row=1, column=1)
        
        self.return_book_button = tk.Button(self.return_book_frame, text="Return Book", command=self.return_book)
        self.return_book_button.grid(row=2, columnspan=2)
        
    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        isbn = self.book_isbn_entry.get()
        self.database.add_book(title, author, isbn)
        messagebox.showinfo("Success", "Book added successfully!")
        
    def add_member(self):
        member_id = self.member_id_entry.get()
        name = self.member_name_entry.get()
        self.database.add_member(member_id, name)
        messagebox.showinfo("Success", "Member added successfully!")
    
    def issue_book(self):
        isbn = self.issue_isbn_entry.get()
        member_id = self.issue_member_id_entry.get()
        self.library.issue_book(isbn, member_id)
    
    def return_book(self):
        isbn = self.return_isbn_entry.get()
        member_id = self.return_member_id_entry.get()
        self.library.return_book(isbn, member_id)

if __name__ == "__main__":
    library = Library()
    admin = Admin("admin", "password")  # Temporary credentials
    root = tk.Tk()
    gui = LibraryGUI(root, library, admin)
    root.mainloop()
