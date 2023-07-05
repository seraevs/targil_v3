# Base image
# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Define an environment variable VERSION
ENV VERSION=1.2.0

# Update apt-get and install vim, zip, and unzip
RUN apt-get update && \
    apt-get install -y vim zip unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy zip_job.py into the image's /app directory
COPY zip_job.py /app/

# Command to print OS type and architecture and verify /app/zip_job.py exists
CMD uname -mrs && if [ -f /app/zip_job.py ]; then echo "/app/zip_job.py exists"; else echo "/app/zip_job.py does not exist"; fi

# Set the entrypoint to execute zip_job.py
ENTRYPOINT ["python", "/app/zip_job.py"]
