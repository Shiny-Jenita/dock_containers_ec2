FROM python:3.12-slim

# Set working directory
WORKDIR /app/data

# Create submissions.json only if it doesn't exist
RUN mkdir -p /app/data && \
    touch submissions.json

# Keep container alive
CMD ["tail", "-f", "/dev/null"]
