FROM python:3.9-slim

WORKDIR /app

# Install dependencies directly
RUN pip install --no-cache-dir \
    requests \
    opentelemetry-distro \
    opentelemetry-exporter-otlp \
    opentelemetry-instrumentation-requests

# Copy the application file
COPY app.py .

# Run the application
CMD ["opentelemetry-instrument", "python", "app.py"]