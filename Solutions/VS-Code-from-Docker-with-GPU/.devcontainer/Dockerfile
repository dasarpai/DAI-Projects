FROM langchain/langchain

# Install any additional packages
RUN apt-get update && apt-get install -y vim nano git

# Set the working directory
WORKDIR /workspace/notion-qa

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install any additional Python dependencies if needed
RUN pip install -e .
