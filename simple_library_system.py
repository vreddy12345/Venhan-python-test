# simple_library_system.py

class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

class Borrower:
    def __init__(self, name, contact_info, membership_id):
        self.name = name
        self.contact_info = contact_info
        self.membership_id = membership_id

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}

    def add_book(self, title, author, isbn, genre, quantity):
        self.books[isbn] = Book(title, author, isbn, genre, quantity)

    def update_book(self, isbn, title=None, author=None, quantity=None):
        book = self.books.get(isbn)
        if book:
            if title: book.title = title
            if author: book.author = author
            if quantity is not None: book.quantity = quantity

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def add_borrower(self, name, contact_info, membership_id):
        self.borrowers[membership_id] = Borrower(name, contact_info, membership_id)

    def update_borrower(self, membership_id, name=None, contact_info=None):
        borrower = self.borrowers.get(membership_id)
        if borrower:
            if name: borrower.name = name
            if contact_info: borrower.contact_info = contact_info

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]

    def borrow_book(self, isbn, membership_id, due_date):
        book = self.books.get(isbn)
        if book and book.quantity > 0:
            book.quantity -= 1
            self.borrowed_books[(isbn, membership_id)] = due_date

    def return_book(self, isbn, membership_id):
        if (isbn, membership_id) in self.borrowed_books:
            self.books[isbn].quantity += 1
            del self.borrowed_books[(isbn, membership_id)]

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results

    def check_availability(self, isbn):
        return self.books[isbn].quantity if isbn in self.books else 0

if __name__ == "__main__":
    library = Library()
    library.add_book("1984", "George Orwell", "123456789", "Dystopian", 3)
    library.add_borrower("Alice Smith", "alice@example.com", "B001")

    library.borrow_book("123456789", "B001", "2024-07-01")

    results = library.search_books(title="1984")
    for book in results:
        print(f"{book.title} by {book.author} - {book.genre} - Available Copies: {book.quantity}")

    library.return_book("123456789", "B001")
