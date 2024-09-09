from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor


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
    provider = OTLPProvider("service_a", "http://localhost:4317")
    trace.set_tracer_provider(provider.provider)

    # instrument the `requests` library for automatic HTTP request tracing.
    RequestsInstrumentor().instrument()
    # LoggingInstrumentor().instrument(set_logging_format=True)
    # HTTPXClientInstrumentor().instrument()


def instrument_fastapi_app(app):
    # This will automatically create spans for incoming HTTP requests and other FastAPI-specific operations
    FastAPIInstrumentor.instrument_app(app)
