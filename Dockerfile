FROM nginx:latest


# Copy your custom HTML file to the container
COPY index.html /usr/share/nginx/html/


# Expose port 80 for incoming HTTP traffic
EXPOSE 80

# Start NGINX when the container starts
CMD ["nginx", "-g", "daemon off;"]


