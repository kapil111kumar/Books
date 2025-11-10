# FastAPI Book CRUD Service

A simple FastAPI application implementing CRUD operations for a `Book` resource using **Tortoise ORM** with **SQLite** and **Aerich** for database migrations.

---

## **Setup Instructions**

You can run the project either **manually** using Python or via **Docker**.

---

### **Approach 1: Manual (Python + venv)**
1. Clone the repository:

```bash
git clone https://github.com/kapil111kumar/Books.git
cd Books
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install aerich
```


4. Initialize Aerich and the database:
```bash
# Initialize Aerich
aerich init -t app.config.TORTOISE_ORM

# Create initial database tables
aerich init-db

# Make and apply migrations
aerich migrate --name <migration_name>
aerich upgrade
```


5. Run the FastAPI app:
```bash
uvicorn app.main:app --reload
```

5. Open your browser: http://127.0.0.1:8000/docs

---
### **Approach 2: Docker (Recommended)**
1. Clone the repository:
```bash
git clone https://github.com/kapil111kumar/Books.git
cd Books
```

2. Make sure Docker Desktop is running.

3. Build and run the container:
```bash
docker-compose build
docker-compose up
```

4. The FastAPI app will run at: http://127.0.0.1:8000/docs

5. Running tests in Docker:
```bash
docker-compose run books-app pytest
```


6. Reset database (optional):
```bash
rm *.db
docker-compose run books-app aerich init-db
 ```
