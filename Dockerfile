FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt . 

RUN pip install --upgrade pip setuptools wheel 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done; uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]