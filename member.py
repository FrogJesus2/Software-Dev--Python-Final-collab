class Member:
    def __init__(self, member_id, name, email, phone, address):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.borrowed_books = []
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        self.borrowed_books.remove(book)
