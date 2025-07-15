FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and web UI
COPY web/ ./web/
COPY models/ ./models/

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "web.main:app", "--host", "0.0.0.0", "--port", "8000"]
