class Book:
    def __init__(self, title: str, author: str, is_checked_out: bool = False) -> None:
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out
