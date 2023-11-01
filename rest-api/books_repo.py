import json
from typing import List

from book_model import Book


class BooksRepo:

    def __init__(self):
        with open('books.json') as books_file:
            data = json.load(books_file)
            self.books: List[Book] = []

            for book in data:
                self.books.append(Book(**book))

    def fetch_all_books(self) -> List[Book]:
        return self.books

    def fetch_book_by_id(self, book_id: int) -> Book | None:
        # read all books from books.json
        for book in self.books:
            if book.id == book_id:
                return book

        return None

    def update_book(self, book_id: int, book: Book) -> Book | None:
        # read all books from books.json
        for index, b in enumerate(self.books):
            if b.id == book_id:
                self.books[index] = book
                return book

        return None

    def delete_book(self, book_id: int) -> bool:
        # read all books from books.json
        for index, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[index]
                return True

        return False

    def create_book(self, book: Book) -> Book:
        # read all books from books.json
        self.books.append(book)
        return book
