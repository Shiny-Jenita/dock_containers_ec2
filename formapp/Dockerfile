FROM nginx:latest

# Remove default Nginx HTML
RUN rm -rf /usr/share/nginx/html/*

# Copy frontend files
COPY . /usr/share/nginx/html/


EXPOSE 80

