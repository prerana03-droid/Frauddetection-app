FROM python:3.9-slim
# Set working directory in container
WORKDIR /app
# Copy requirements file
COPY requirements.txt . .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy application files
COPY fraud_detection.py .
COPY Fraud_detection_model.pkl .
# Expose Streamlit default port
EXPOSE 8501
# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run the Streamlit app
CMD ["streamlit", "run", "fraud_detection.py", "--server.address=0.0.0.0"]