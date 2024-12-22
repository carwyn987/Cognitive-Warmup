# Use Python as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy application code and install dependencies
COPY requirements.txt requirements.txt
RUN python3.10 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod 777 /app
RUN chmod 777 /app/output/output.txt

# Command to run the app
ENTRYPOINT ["python", "main.py", "--config_file=/app/config/tasking.yaml", "/app/source", "/app/output"]