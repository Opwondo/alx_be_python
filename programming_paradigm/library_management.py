class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        """Check out the book if it's available"""
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book if it was checked out"""
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def __str__(self):
        status = "checked out" if self.is_checked_out else "available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self._books = []  # Change this to _books (private attribute)

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, isbn):
        self._books = [b for b in self._books if b.isbn != isbn]

    def list_books(self):
        return self._books

    def check_out_book(self, isbn):
        """Check out a book by ISBN"""
        for book in self._books:
            if book.isbn == isbn:
                return book.check_out()
        return False

    def return_book(self, isbn):
        """Return a book by ISBN"""
        for book in self._books:
            if book.isbn == isbn:
                return book.return_book()
        return False