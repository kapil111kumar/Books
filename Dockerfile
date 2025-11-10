# Use official Python 3.12 image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run migrations then start the app
CMD ["sh", "-c", "aerich upgrade && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
