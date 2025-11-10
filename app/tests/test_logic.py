import pytest
from app import crud
from app.models import Book

@pytest.mark.asyncio
async def test_create_and_count_book():
    # Create a book
    book = await crud.create_book("Test Book", "Description")
    assert book.title == "Test Book"

    # Custom SQL query test
    count = await crud.count_books_with_keyword("Test")
    assert count == 1
