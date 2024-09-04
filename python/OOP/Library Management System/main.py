from models.book import Book
from models.library import Library
from models.member import Member


def create_library() -> Library:
    library = Library()
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
    ]

    for book in books:
        library.add_book(book)

    return library


if __name__ == "__main__":
    library = create_library()

    print("Books available in the library:")
    for book in library.list_available_books():
        print(book.title)
    print("\n")

    alice = Member("Alice")
    bob = Member("Bob")

    book1 = library.find_book_by_title("The Great Gatsby")
    book2 = library.find_book_by_title("To Kill a Mockingbird")
    book3 = library.find_book_by_title("1984")


    alice.borrow_book(book1)

    bob.borrow_book(book2)
    bob.borrow_book(book3)

    bob.return_book(book2)

    print("Books available in the library:")
    for book in library.list_available_books():
        print(book.title)
    print("\n")

    print("Books borrowed by Alice:")
    for book in alice.borrowed_books:
        print(book.title)
    print("\n")

    print("Books borrowed by Bob:")
    for book in bob.borrowed_books:
        print(book.title)
