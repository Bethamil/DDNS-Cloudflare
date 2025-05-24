# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Install cron
RUN apt-get update && apt-get install -y cron

# Copy the cron file to the cron.d directory
COPY crontab.txt /etc/cron.d/cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD sh -c "printenv | grep -E 'API_TOKEN|NAME|ZONE' | sed 's/^/export /' > /app/env.sh && cron && tail -f /var/log/cron.log"
