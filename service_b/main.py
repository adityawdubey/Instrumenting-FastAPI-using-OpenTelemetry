from fastapi import FastAPI
from otel_config import configure_instrumentation, instrument_fastapi_app

# Configure OpenTelemetry instrumentation
configure_instrumentation()

app = FastAPI()

# Instrument FastAPI for OpenTelemetry
instrument_fastapi_app(app)

@app.get("/service_b")
def service_b_endpoint():
    return {"message": "Hello from Service B"}
