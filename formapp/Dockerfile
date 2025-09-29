# Use official Nginx image
FROM nginx:alpine

# Copy your frontend files to Nginx html directory
COPY . /usr/share/nginx/html

# Copy custom Nginx config if needed
# COPY default.conf /etc/nginx/conf.d/default.conf

# Expose port 80 (will be mapped to 8080 in Docker Compose)
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]



