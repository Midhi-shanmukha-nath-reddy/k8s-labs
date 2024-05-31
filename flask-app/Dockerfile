# Use the official Amazon Linux image
FROM amazonlinux:2

# Install Python and other dependencies
RUN yum -y install \
    python3 \
    python3-pip \
    && yum clean all

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip3 install flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]

