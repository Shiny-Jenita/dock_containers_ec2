# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . /app

# Expose port
EXPOSE 8000

# Run your server
CMD ["python", "server.py"]
