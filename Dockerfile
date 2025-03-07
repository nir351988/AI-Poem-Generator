# Use an official Python slim image
FROM python:3.10-slim

# Install build dependencies and required system packages (if needed)
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy only requirements first for caching dependency installs
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn for production serving
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the application code
COPY . .

# Create a non-root user and switch to it (adjust UID/GID as needed)
RUN useradd --create-home appuser
USER appuser

# Expose the port (adjust if your app listens on a different port)
EXPOSE 5000

# Set environment variables (can be overridden by docker-compose or .env file)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Optionally, set FLASK_ENV=production

# For production, run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]