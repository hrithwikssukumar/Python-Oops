class Library:
    def __init__(self):
        self.books = []  # List to store available books
        self.borrowed_books = {}  # Dictionary to store borrowed books and borrowers

    # Method to add a new book to the library
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'Book "{book_name}" has been added to the library.')

    # Method to borrow a book from the library
    def borrow_book(self, book_name, borrower):
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books[book_name] = borrower
            print(f'Book "{book_name}" has been borrowed by {borrower}.')
        elif book_name in self.borrowed_books:
            print(f'Sorry, the book "{book_name}" is already borrowed by {self.borrowed_books[book_name]}.')
        else:
            print(f'Sorry, the book "{book_name}" is not available in the library.')

    # Method to return a borrowed book to the library
    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            borrower = self.borrowed_books.pop(book_name)
            self.books.append(book_name)
            print(f'Book "{book_name}" has been returned by {borrower}.')
        else:
            print(f'The book "{book_name}" was not borrowed.')

    # Method to display available books in the library
    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")


# Example usage
library = Library()

# Adding books to the library
library.add_book("Python Programming")
library.add_book("Data Science Basics")
library.add_book("AI for Beginners")

# Displaying available books
library.display_books()

# Borrowing a book
library.borrow_book("Python Programming", "Hrithwik")

# Trying to borrow the same book again
library.borrow_book("Python Programming", "Virat")

# Displaying available books after borrowing
library.display_books()

# Returning a book
library.return_book("Python Programming")

# Displaying available books after returning
library.display_books()
