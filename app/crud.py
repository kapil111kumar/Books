from app.models import Book
from tortoise.transactions import in_transaction
from typing import List, Optional
from tortoise.queryset import QuerySet

# Create a book with transaction handling
async def create_book(title: str, description: Optional[str] = None) -> Book:
    async with in_transaction("default"):  # specify connection to avoid ParamsError
        return await Book.create(title=title, description=description)

# Get all books
async def get_books(
    limit: int = 10,
    offset: int = 0,
    title_filter: Optional[str] = None,
    sort_by: str = "id",
    sort_order: str = "asc",
) -> List[Book]:
    query: QuerySet = Book.all()

    # Apply title filter
    if title_filter:
        query = query.filter(title__icontains=title_filter)

    # Apply sorting
    if sort_order == "desc":
        query = query.order_by(f"-{sort_by}")
    else:
        query = query.order_by(sort_by)

    return await query.offset(offset).limit(limit)

# Get single book
async def get_book(book_id: int) -> Optional[Book]:
    return await Book.filter(id=book_id).first()

# Update a book
async def update_book(book_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Book]:
    book = await get_book(book_id)
    if not book:
        return None
    if title is not None:
        book.title = title
    if description is not None:
        book.description = description
    await book.save()
    return book

# Delete a book
async def delete_book(book_id: int) -> bool:
    deleted_count = await Book.filter(id=book_id).delete()
    return deleted_count > 0

# Custom query example
async def count_books_with_keyword(keyword: str) -> int:
    return await Book.filter(title__icontains=keyword).count()
