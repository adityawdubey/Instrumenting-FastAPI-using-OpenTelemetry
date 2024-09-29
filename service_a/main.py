from fastapi import FastAPI
import requests
from otel_config import configure_instrumentation, instrument_fastapi_app

# Configure OpenTelemetry instrumentation
configure_instrumentation()

app = FastAPI()

# Instrument FastAPI for OpenTelemetry
instrument_fastapi_app(app)

@app.get("/call-service-b")
def call_service_b():
    # Make a request to Service B (running on port 8001)
    response = requests.get("http://localhost:8001/service_b")
    return {"response_from_service_b": response.json()}
