# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run streamlit with the --server.runOnSave flag to enable live reloading
CMD ["streamlit", "run", "bike_customizer.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.runOnSave=true"] 