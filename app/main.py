from fastapi import Depends, FastAPI, HTTPException, Query
from tortoise.contrib.fastapi import register_tortoise
from app import models, schemas, crud
from app.config import DATABASE_URL
from typing import List, Optional
from app.auth import verify_api_key

app = FastAPI(title="Book CRUD API")


# Routes
@app.post("/books/", response_model=schemas.BookOut, status_code=201, dependencies=[Depends(verify_api_key)])
async def create_book(book: schemas.BookCreate):
    existing = await models.Book.filter(title=book.title).first()
    if existing:
        raise HTTPException(status_code=400, detail="Book with this title already exists")
    return await crud.create_book(book.title, book.description)


@app.get("/books/", response_model=List[schemas.BookOut])
async def list_books(
        limit: int = 10,
        offset: int = 0,
        title: Optional[str] = Query(None, description="Filter books by title containing this string"),
        sort_by: Optional[str] = Query("id", description="Field to sort by: id, title, created_at"),
        sort_order: Optional[str] = Query("asc", description="Sort order: asc or desc"),
):
    return await crud.get_books(limit=limit, offset=offset, title_filter=title, sort_by=sort_by, sort_order=sort_order)


@app.get("/books/{book_id}", response_model=schemas.BookOut)
async def get_book(book_id: int):
    book = await crud.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}", response_model=schemas.BookOut, dependencies=[Depends(verify_api_key)])
async def update_book(book_id: int, book_update: schemas.BookUpdate):
    updated = await crud.update_book(book_id, book_update.title, book_update.description)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated


@app.delete("/books/{book_id}", status_code=204, dependencies=[Depends(verify_api_key)])
async def delete_book(book_id: int):
    deleted = await crud.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return None


# Tortoise ORM initialization
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
