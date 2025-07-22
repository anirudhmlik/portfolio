# Use official Python image as a base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "portfolio.py", "--server.port=8501", "--server.address=0.0.0.0"]
