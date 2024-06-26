# Use the official Python 3.11 image from the Docker library
FROM python:3.11

# Set the working directory in the Docker container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install the Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Command to run the application(Get-ECRLoginCommand).Password | docker login --username AWS --password-stdin public.ecr.aws/z3d8h0g3
# AWS App runner expects port 8080 and host 0.0.0.0
CMD ["python3", "-m", "chainlit", "run", "chatbot.py", "--port", "8080", "--host", "0.0.0.0"]

### Load in the terminal

#docker buildx build . --platform linux/amd64 -t twijnands1/chatbot:latest
#docker push twijnands1/chatbot:latest

