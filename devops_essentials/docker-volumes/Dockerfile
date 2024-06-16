# Use the Alpine base image
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Add the config.txt file to /app/config.txt
COPY config.txt /app/config.txt

# Specify a volume at /data
VOLUME /data

# Set a default command for the container
CMD ["echo", "Container is ready!"]
