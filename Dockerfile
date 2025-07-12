FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY req_for_docker/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . /app

# Expose port for FastAPI
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
