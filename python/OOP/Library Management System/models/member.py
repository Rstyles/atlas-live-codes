from models.book import Book


class Member:
    def __init__(self, name: str) -> None:
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book) -> None:
        if book.is_checked_out:
            raise ValueError(f"Book {book.title} is already checked out")
        book.is_checked_out = True
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        book.is_checked_out = False
        self.borrowed_books.remove(book)
