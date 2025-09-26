FROM python:3.9-slim

WORKDIR /app

COPY server.py .

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["python", "server.py"]
