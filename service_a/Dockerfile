# Stage 1: Build stage
FROM python:3.10-slim AS builder

WORKDIR /usr/src/app

# Copy only the requirements file first to leverage Docker cache
COPY service_a/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY service_a ./service_a

# Stage 2: Final stage
FROM python:3.10-slim

WORKDIR /usr/src/app

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/src/app/service_a ./service_a

EXPOSE 8000

CMD ["uvicorn", "service_a.main:app", "--host", "0.0.0.0", "--port", "8000"]
