# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose both ports
EXPOSE 8000
EXPOSE 8501

# Default command starts both apps using a shell script
CMD ["sh", "start.sh"]