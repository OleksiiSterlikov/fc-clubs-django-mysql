# Python official runtime image
FROM python:3.12

# Set environment variables
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Create the app directoty
RUN mkdir /fc_clubs

# Set the working directory
WORKDIR /fc_clubs

# Add all files project directory to the working directory
ADD . /fc_clubs

# Run command to install all dependencys and upgrade packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run command to install Mysql Client packages
RUN pip install mysqlclient

# Copy Project to the container
COPY . /fc_clubs

#ENTRYPOINT ["./docker/entrypoint.sh"]