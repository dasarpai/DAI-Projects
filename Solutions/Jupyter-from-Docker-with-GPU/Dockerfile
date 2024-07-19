FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Install Python 3.9 and necessary dependencies
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-distutils \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.9
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.9 get-pip.py && rm get-pip.py

# Set Python 3.9 as the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Install Jupyter Notebook and JupyterLab
RUN pip install notebook jupyterlab

# Install other required Python packages
RUN pip install -U langchain-nomic langchain_community tiktoken langchainhub chromadb langchain langchain-text-splitters tavily-python nomic[local]

# Copy the Jupyter configuration file (if you have one)
# COPY jupyter_notebook_config.py /root/.jupyter/

# Set the working directory
WORKDIR /workspace

# Expose the port for Jupyter
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
