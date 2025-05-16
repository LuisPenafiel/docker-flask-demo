FROM python:3.8-slim

WORKDIR /app

# Instalar dependencias del sistema, incluyendo git
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "app.py"]