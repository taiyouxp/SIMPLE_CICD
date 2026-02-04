# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install fastapi uvicorn httpx pytest

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]