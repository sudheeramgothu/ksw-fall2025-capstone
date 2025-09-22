# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Run Flask app with Gunicorn (1 worker, 2 threads)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers=2", "--threads=2"]
