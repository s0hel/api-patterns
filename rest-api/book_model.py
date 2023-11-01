from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str | None = None
    author: str | None = None
    isbn: str | None = None
    publisher: str | None = None
