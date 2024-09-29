FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r service_b/requirements.txt

EXPOSE 8001

CMD ["uvicorn", "service_b.main:app", "--host", "0.0.0.0", "--port", "8001"]