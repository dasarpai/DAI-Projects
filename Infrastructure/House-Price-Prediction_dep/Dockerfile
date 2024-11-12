# Use the official Python image with Python 3.9
FROM python:3.9-slim

# Set the environment variable to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Upgrade pip and install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

# Add the application code and other necessary files
COPY ./app.py /
COPY ./kc_house_data.csv /
COPY ./model_houseprice.pkl /
COPY ./config.json /

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python3", "-u", "./app.py"]
