import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.kafka import KafkaInstrumentor


class OTLPProvider:
    """
    Configures OpenTelemetry with OTLP Exporter.
    """
    def __init__(
            self,
            service_name: str,
            exporter_endpoint: str,
    ) -> None:
    
        self._provider = TracerProvider(
            resource=Resource(attributes={SERVICE_NAME: service_name}),
            active_span_processor=BatchSpanProcessor(
                OTLPSpanExporter(
                    endpoint=exporter_endpoint,
                )
            ),
        )

    @property
    def provider(self) -> TracerProvider:
        return self._provider


def configure_instrumentation():
    """
    Configures OpenTelemetry instrumentation for requests and FastAPI.
    """
    # tempo_endpoint = os.getenv('TEMPO_ENDPOINT', 'http://localhost:4317')
    # tempo_endpoint = os.getenv('TEMPO_ENDPOINT', 'http://tempo-query-frontend.fastapi.svc.cluster.local:3100')
    tempo_endpoint = os.getenv('TEMPO_ENDPOINT', 'http://tempo.fastapi.svc.cluster.local:4317')
    provider = OTLPProvider("service_b", tempo_endpoint)
    trace.set_tracer_provider(provider.provider)

# Instrument HTTP requests, HTTPX client, and Kafka to enable tracing
    RequestsInstrumentor().instrument()
    HTTPXClientInstrumentor().instrument()
    KafkaInstrumentor().instrument()


def instrument_fastapi_app(app):
    # This will automatically create spans for incoming HTTP requests and other FastAPI-specific operations
    FastAPIInstrumentor.instrument_app(app)
