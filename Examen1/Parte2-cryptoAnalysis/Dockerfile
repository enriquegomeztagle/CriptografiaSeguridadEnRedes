FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "criptoAnalysis-base64-des-cbc3.py"]
