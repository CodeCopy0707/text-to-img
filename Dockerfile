# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && apt-get clean

# Clone the Stable Diffusion Lite repository
RUN git clone https://github.com/basujindal/stable-diffusion-cpu.git /app/stable-diffusion

# Set working directory inside the cloned repo
WORKDIR /app/stable-diffusion

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Start the app in CPU mode
CMD ["python", "app.py", "--port", "8080", "--cpu"]
