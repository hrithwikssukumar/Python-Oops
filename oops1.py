class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.title}' has been returned.")







class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print(f"Books in {self.name} Library:")
            for book in self.books:
                book.display_info()
                print("-" * 30)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found.")
        return None



# Create a library
my_library = Library("City Library")

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# List all books
my_library.list_books()

# Borrow a book
book_to_borrow = my_library.find_book("1984")
if book_to_borrow:
    book_to_borrow.borrow_book()

# Try to borrow the same book again
book_to_borrow.borrow_book()

# Return the book
book_to_borrow.return_book()

# List books again to see updated availability
my_library.list_books()
