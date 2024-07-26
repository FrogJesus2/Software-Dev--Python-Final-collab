import tkinter as tk
import re
from tkinter import messagebox
from library import Library
from book import Book
from member import Member
from datetime import date

def validate_email(email):  
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  
        return True  
    return False  

def isValid(phone):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(phone) is not None

class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.transactions = []
        self.transaction_id = 0
        self.root.title("Library Management System")
        
        # Add book section
        self.add_book_frame = tk.Frame(root)
        self.add_book_frame.pack()

        self.book_isbn_label = tk.Label(self.add_book_frame, text="Book ISBN")
        self.book_isbn_label.grid(row=0, column=0)
        self.book_isbn_entry = tk.Entry(self.add_book_frame)
        self.book_isbn_entry.grid(row=0, column=1)
        
        self.book_title_label = tk.Label(self.add_book_frame, text="Book Title")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = tk.Entry(self.add_book_frame)
        self.book_title_entry.grid(row=1, column=1)
        
        self.book_author_label = tk.Label(self.add_book_frame, text="Book Author")
        self.book_author_label.grid(row=2, column=0)
        self.book_author_entry = tk.Entry(self.add_book_frame)
        self.book_author_entry.grid(row=2, column=1)

        self.book_genre_label = tk.Label(self.add_book_frame, text="Book Genre")
        self.book_genre_label.grid(row=3, column=0)
        self.book_genre_entry = tk.Entry(self.add_book_frame)
        self.book_genre_entry.grid(row=3, column=1)
        
        
        self.add_book_button = tk.Button(self.add_book_frame, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=4, columnspan=2)

        self.book_remove_isbn_label = tk.Label(self.add_book_frame, text="Book ISBN")
        self.book_remove_isbn_label.grid(row=5, column=0)
        self.book_remove_isbn_entry = tk.Entry(self.add_book_frame)
        self.book_remove_isbn_entry.grid(row=5, column=1)

        self.remove_book_button = tk.Button(self.add_book_frame, text="Remove Book", command=self.remove_book)
        self.remove_book_button.grid(row=6, columnspan=2)

        self.add_book_button = tk.Button(self.add_book_frame, text="Book List", command=self.book_list)
        self.add_book_button.grid(row=7, columnspan=2)
        
        # Add member section
        self.add_member_frame = tk.Frame(root)
        self.add_member_frame.pack()
        
        self.member_id_label = tk.Label(self.add_member_frame, text="Member ID")
        self.member_id_label.grid(row=0, column=0)
        self.member_id_entry = tk.Entry(self.add_member_frame)
        self.member_id_entry.grid(row=0, column=1)
        
        self.member_name_label = tk.Label(self.add_member_frame, text="Member Name")
        self.member_name_label.grid(row=1, column=0)
        self.member_name_entry = tk.Entry(self.add_member_frame)
        self.member_name_entry.grid(row=1, column=1)

        self.member_email_label = tk.Label(self.add_member_frame, text="Member Email")
        self.member_email_label.grid(row=2, column=0)
        self.member_email_entry = tk.Entry(self.add_member_frame)
        self.member_email_entry.grid(row=2, column=1)

        self.member_phone_label = tk.Label(self.add_member_frame, text="Member Phone")
        self.member_phone_label.grid(row=3, column=0)
        self.member_phone_entry = tk.Entry(self.add_member_frame)
        self.member_phone_entry.grid(row=3, column=1)

        self.member_address_label = tk.Label(self.add_member_frame, text="Member Address")
        self.member_address_label.grid(row=4, column=0)
        self.member_address_entry = tk.Entry(self.add_member_frame)
        self.member_address_entry.grid(row=4, column=1)
        
        self.add_member_button = tk.Button(self.add_member_frame, text="Add Member", command=self.add_member)
        self.add_member_button.grid(row=5, columnspan=2)

        self.member_remove_id_label = tk.Label(self.add_member_frame, text="Member ID")
        self.member_remove_id_label.grid(row=6, column=0)
        self.member_remove_id_entry = tk.Entry(self.add_member_frame)
        self.member_remove_id_entry.grid(row=6, column=1)

        self.remove_member_button = tk.Button(self.add_member_frame, text="Remove Member", command=self.remove_member)
        self.remove_member_button.grid(row=7, columnspan=2)

        self.add_member_button = tk.Button(self.add_member_frame, text="Member List", command=self.member_list)
        self.add_member_button.grid(row=8, columnspan=2)
        
        # Issue book section
        self.issue_book_frame = tk.Frame(root)
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
        self.return_book_frame = tk.Frame(root)
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

        self.return_book_button = tk.Button(self.return_book_frame, text="Transactions", command=self.transaction_list)
        self.return_book_button.grid(row=3, columnspan=2)
        
        
    def add_book(self):
        title = self.book_title_entry.get()
        author = self.book_author_entry.get()
        genre = self.book_genre_entry.get()
        isbn = self.book_isbn_entry.get()
        if not isbn.isdigit():
            messagebox.showerror("Error", "ISBN must be an integer!")
            return
        book = Book(title, author, genre, isbn)
        
        self.library.add_book(book)
        
        messagebox.showinfo("Success", "Book added successfully!")
    
    # Calls remove_book after getting the text in the entry box.
    def remove_book(self):
        isbn = self.book_remove_isbn_entry.get()
        if not isbn.isdigit():
            messagebox.showerror("Error", "ISBN must be an integer!")
            return
        self.library.remove_book(isbn)

    # Uses a for loop to display all the books in a list in another window using tk.Toplevel
    def book_list(self):
        book_list = tk.Toplevel(self.root)
        book_list.title("Book Collection")

        book_listbox = tk.Listbox(book_list, width=75, height=20)
        book_listbox.pack(padx=10, pady=10)

        for isbn, book in self.library.books.items():
            book_listbox.insert(tk.END, f"Book Title: {book.title}, Book Author: {book.author}, Book Genre: {book.genre}, ISBN: {book.isbn}")

    def add_member(self):
        member_id = self.member_id_entry.get()
        if not member_id.isdigit():
            messagebox.showerror("Error", "Member ID must be an integer!")
            return
        name = self.member_name_entry.get()
        email = self.member_email_entry.get()

        if not validate_email(email):
            messagebox.showerror("Error", "That email is not valid.")
            return
        
        phone = self.member_phone_entry.get()

        if not isValid(phone):
            messagebox.showerror("Error", "That phone number is not valid.")
            return
        
        address = self.member_address_entry.get()
        member = Member(member_id, name, email, phone, address)
        self.library.add_member(member)
        messagebox.showinfo("Success", "Member added successfully!")
    
    # Calls remove_member after getting the text in the entry box.
    def remove_member(self):
        member_id = self.member_remove_id_entry.get()
        if not member_id.isdigit():
            messagebox.showerror("Error", "Member ID must be an integer!")
            return
        self.library.remove_member(member_id)

    # Uses a for loop to display all the members in a list in another window using tk.Toplevel
    def member_list(self):
        member_list = tk.Toplevel(self.root)
        member_list.title("Member List")

        member_listbox = tk.Listbox(member_list, width=75, height=20)
        member_listbox.pack(padx=10, pady=10)

        for member_id, member in self.library.members.items():
            member_listbox.insert(tk.END, f"Member Name: {member.name}, Email: {member.email}, Phone Number: {member.phone}, Address: {member.address}, ID: {member.member_id}")

    # I updated the issue_book function to include storing information for a transaction list in a dictionary
    def issue_book(self):
        isbn = self.issue_isbn_entry.get()
        if not isbn.isdigit():
            messagebox.showerror("Error", "ISBN must be an integer!")
            return
        member_id = self.issue_member_id_entry.get()
        if not member_id.isdigit():
            messagebox.showerror("Error", "Member ID must be an integer!")
            return
        self.library.issue_book(isbn, member_id)
        self.transaction_id += 1
        today = date.today()
        transaction_list = {
            'transaction_id': self.transaction_id,
            'isbn': isbn,
            'member_id': member_id,
            'date': today,
        }
        self.transactions.append(transaction_list)
        return transaction_list
    # I basically did the same thing with return, they both give a unique transaction id that gets incremented every time someone borrows or returns a book
    def return_book(self):
        isbn = self.return_isbn_entry.get()
        if not isbn.isdigit():
            messagebox.showerror("Error", "ISBN must be an integer!")
            return
        member_id = self.return_member_id_entry.get()
        if not member_id.isdigit():
            messagebox.showerror("Error", "Member ID must be an integer!")
            return
        self.library.return_book(isbn, member_id)
        self.transaction_id += 1
        today = date.today()
        transaction_list = {
            'transaction_id': self.transaction_id,
            'isbn': isbn,
            'member_id': member_id,
            'date': today,
        }
        self.transactions.append(transaction_list)
        return transaction_list

    # The function we call to open in another tkinter window to see all transactions
    def transaction_list(self):
        transactions_list = tk.Toplevel(self.root)
        transactions_list.title("Member List")

        transaction_listbox = tk.Listbox(transactions_list, width=75, height=20)
        transaction_listbox.pack(padx=10, pady=10)

        for transaction in self.transactions:
            transaction_info = f"Transaction ID: {transaction['transaction_id']}, ISBN: {transaction['isbn']}, Member ID: {transaction['member_id']}, Member ID: {transaction['date']}"
            transaction_listbox.insert(tk.END, transaction_info)
    


if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    gui = LibraryGUI(root, library)
    root.mainloop()
