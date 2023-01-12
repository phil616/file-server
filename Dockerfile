# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# Install the app's dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install uvicorn python-multipart aiomysql

# Copy the rest of the app's code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 80

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]