class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and attempts to check it out."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available or does not exist in the library.")

    def return_book(self, title):
        """Finds a book by title and attempts to return it."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' is either not checked out or not in the library.")

    def list_available_books(self):
        """Prints all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

