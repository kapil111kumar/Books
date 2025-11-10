DATABASE_URL = "sqlite://db.sqlite3"
API_KEY = "supersecretapikey"  # 🔒 Change to anything secure
API_KEY_NAME = "X-API-Key"

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        }
    },
}
