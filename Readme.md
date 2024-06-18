# Simple Library Management System

## Overview
This is a basic library management system implemented using Python. It supports adding, updating, and removing books and borrowers, as well as borrowing and returning books. Additionally, it includes a search feature to find books by title, author, or genre.

## Features
- **Book Management**: Add, update, and remove books.
- **Borrower Management**: Add, update, and remove borrowers.
- **Book Borrowing and Returning**: Borrow books, record due dates, and return books.
- **Book Search and Availability**: Search for books and check their availability.

## Usage
1. Clone the repository:
   ```sh
   git clone <repository-url>

2. Navigate to the project directory:
   
   cd simple-library-management-system

3. Run the script
 
    python simple_library_system.py


Here is an example of how to use the system:

library = Library()
library.add_book("1984", "George Orwell", "123456789", "Dystopian", 3)
library.add_borrower("Alice Smith", "alice@example.com", "B001")

# Borrow a book
library.borrow_book("123456789", "B001", "2024-07-01")

# Search for a book
results = library.search_books(title="1984")
for book in results:
    print(f"{book.title} by {book.author} - {book.genre} - Available Copies: {book.quantity}")

# Return a book
library.return_book("123456789", "B001")
