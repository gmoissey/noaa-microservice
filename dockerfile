FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py .
COPY app/ ./app/

EXPOSE 5001

CMD ["python", "run.py"]
