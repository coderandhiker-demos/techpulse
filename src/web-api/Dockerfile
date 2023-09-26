# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src/web-api/ /app 
COPY pyproject.toml /app/
COPY poetry.lock /app/

# Update the image OS
RUN apt-get update && \
    apt-get upgrade -y

# Install any needed packages specified in requirements.txt
RUN pip install poetry && poetry install

# Make port 60010 available to the world outside this container
EXPOSE 60010

# Run the application using poetry 
# this is a dev configuration - we'd use poetry publish and the dist folder for prod
CMD ["poetry", "run", "python", "app.py"]
