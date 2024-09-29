FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r service_a/requirements.txt

EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "service_a.main:app", "--host", "0.0.0.0", "--port", "8000"]
