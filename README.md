# FastAPI Book CRUD Service

A simple FastAPI application implementing CRUD operations for a `Book` resource using **Tortoise ORM** with **SQLite** and **Aerich** for database migrations.

---

## **Setup Instructions**

### **1. Clone the repository**

```bash
git clone <repo-url>
cd <repo-folder>

python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\activate         # Windows

pip install -r requirements.txt


pip install aerich

# Initialize Aerich
aerich init -t app.config.TORTOISE_ORM

# Create initial database tables
aerich init-db

aerich migrate --name <migration_name>

# Apply migration
aerich upgrade


uvicorn app.main:app --reload
