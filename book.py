class Book:
    def __init__(self, title, author, genre, isbn):
        self.details = (title, author, genre, isbn)  # Using a tuple to store book details
        self.issued_to = None
        self.list_details = list(self.details)

    @property
    def title(self):
        return self.details[0]

    @property
    def author(self):
        return self.details[1]
    
    @property
    def genre(self):
        return self.details[2]
    
    @property
    def isbn(self):
        return self.details[3]
    
    def isbn_setter(self, value):
        try:
            self._isbn = int(value)
        except ValueError:
            raise ValueError("isbn must be integer, please re-enter value.")

    
    def issue(self, member):
        self.issued_to = member
    
    def return_book(self):
        self.issued_to = None




