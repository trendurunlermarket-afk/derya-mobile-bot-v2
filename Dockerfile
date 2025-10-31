# Use Python runtime
FROM python:3.11-slim

WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run main script
CMD ["python", "main.py"]
