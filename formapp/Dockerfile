FROM python:3.11-slim

WORKDIR /app

# Copy HTML and static files
COPY index.html /app/

# Expose frontend port
EXPOSE 8080

# Run Python's built-in HTTP server
CMD ["python", "-m", "http.server", "8080"]


