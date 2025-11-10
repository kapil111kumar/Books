import pytest
from app.main import app
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

@pytest.mark.asyncio
async def test_create_and_get_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Create book
        response = await ac.post("/books/", json={"title": "API Book", "description": "desc"})
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "API Book"

        # Get the book
        book_id = data["id"]
        get_response = await ac.get(f"/books/{book_id}")
        assert get_response.status_code == 200
        assert get_response.json()["title"] == "API Book"
