# Stage 1: Build dependencies
FROM python:3.10-slim as builder

WORKDIR /usr/src/app

# Copy only the requirements file first to leverage Docker cache
COPY service_b/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.10-slim

WORKDIR /usr/src/app

# Copy installed dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy only necessary files
COPY service_b ./service_b

EXPOSE 8001

CMD ["uvicorn", "service_b.main:app", "--host", "0.0.0.0", "--port", "8001"]