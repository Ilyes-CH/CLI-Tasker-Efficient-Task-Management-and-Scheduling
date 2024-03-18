# Use Alpine Linux as the base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the required files into the container
COPY .env .
COPY req.txt .
COPY src/SMS_Sender.py .
COPY Todo_app.py .

# Install required packages
RUN apk --no-cache add build-base
RUN pip install --no-cache-dir -r req.txt

# Expose any required ports (if your app uses any)

# Set environment variables
ENV ACCOUNT_SID=""
ENV AUTH=""

# Start the SMS sender in the background
CMD ["python", "SMS_Sender.py"] 
