from fastapi import FastAPI
from books_repo import BooksRepo
from book_model import Book

app = FastAPI()

book_repo = BooksRepo()


# api to get list of books
@app.get("/books")
async def fetch_books():
    return book_repo.fetch_all_books()


# api to get book by id
@app.get("/books/{book_id}")
async def fetch_book_by_id(book_id: int):
    return book_repo.fetch_book_by_id(book_id)


# update book
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    return book_repo.update_book(book_id, book)


# delete book
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    return book_repo.delete_book(book_id)


# create book
@app.post("/books")
async def create_book(book: Book):
    return book_repo.create_book(book)
