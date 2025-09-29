FROM python:3.9-slim

WORKDIR /app

# Copy server.py into /app
COPY server.py /app/

COPY submission.json /app/

# Create a folder for data if your app writes files
RUN mkdir -p /app/data

EXPOSE 5000

CMD ["python", "server.py"]

