# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY check_license_service.py /app/

# Install dependencies
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "check_license_service.py"]
