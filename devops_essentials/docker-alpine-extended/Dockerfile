# Use the Alpine base image
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Add the config.txt file to /app/config.txt
COPY config.txt /app/config.txt

# Set a default command for the container
CMD ["echo", "Container is ready!"]
