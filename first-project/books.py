from fastapi import FastAPI
from typing import Optional

app = FastAPI()

BOOKS = [
    {"title": "Title 1", "author": "Auhtor 1", "category": "science"},
    {"title": "Title 2", "author": "Auhtor 2", "category": "science"},
    {"title": "Title 3", "author": "Auhtor 3", "category": "science"},
    {"title": "Title 4", "author": "Auhtor 4", "category": "science"},
    {"title": "Title 5", "author": "Auhtor 5", "category": "science"},
    {"title": "Title 6", "author": "Auhtor 6", "category": "science"}
]


@app.get("/books")
async def read_all_books(category: Optional[str] = None):
    if not category:
        return BOOKS

    filtered_books = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            filtered_books.append(book)

    return filtered_books


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"error": "Book not Found"}
