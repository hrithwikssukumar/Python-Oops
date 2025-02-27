class Library:
    def __init__(self):
        self.books = []  
        self.borrowed_books = {}  

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'Book "{book_name}" has been added to the library.')


    def borrow_book(self, book_name, borrower):
        if book_name in self.books:
            self.books.remove(book_name)
            self.borrowed_books[book_name] = borrower
            print(f'Book "{book_name}" has been borrowed by {borrower}.')
        elif book_name in self.borrowed_books:
            print(f'Sorry, the book "{book_name}" is already borrowed by {self.borrowed_books[book_name]}.')
        else:
            print(f'Sorry, the book "{book_name}" is not available in the library.')

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            borrower = self.borrowed_books.pop(book_name)
            self.books.append(book_name)
            print(f'Book "{book_name}" has been returned by {borrower}.')
        else:
            print(f'The book "{book_name}" was not borrowed.')

    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")



library = Library()


library.add_book("Python Programming")
library.add_book("Data Science Basics")
library.add_book("AI for Beginners")


library.display_books()

library.borrow_book("Python Programming", "Hrithwik")


library.borrow_book("Python Programming", "Virat")


library.display_books()


library.return_book("Python Programming")


library.display_books()
