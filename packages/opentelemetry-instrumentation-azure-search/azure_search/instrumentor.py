from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from azure.search.documents import SearchClient

class AzureSearchInstrumentor(BaseInstrumentor):
    def __init__(self):
        super().__init__()

    def _instrument(self, tracer_provider, **kwargs):
        pass

    def _uninstrument(self, tracer_provider, **kwargs):
        pass

