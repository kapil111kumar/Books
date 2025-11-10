import pytest
from tortoise import Tortoise

# Initialize Tortoise ORM for tests
@pytest.fixture(scope="module", autouse=True)
async def init_db():
    """
    Initialize an in-memory SQLite database for testing.
    """
    await Tortoise.init(
        db_url="sqlite://:memory:",
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()
