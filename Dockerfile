FROM python:3.9-slim

WORKDIR /app

COPY . .
COPY requirements.txt .
COPY data.json .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]