from models.book import Book


class Library:
    books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def find_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
        raise ValueError(f"Book with title {title} not found")
    
    def list_available_books(self) -> list[Book]:
        return [book for book in self.books if not book.is_checked_out]
