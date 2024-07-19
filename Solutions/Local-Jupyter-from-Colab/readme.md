# Install Jupyter on your local machine:

bash
pip install jupyter

# Install Jupyter HTTP-over-WebSocket extension:

bash
pip install jupyter_http_over_ws
jupyter serverextension enable --py jupyter_http_over_ws

# Start Jupyter notebook on your local machine:
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888

# Connect Colab to the local runtime:

In Google Colab, go to Edit > Notebook settings and set the Hardware accelerator to None. Then, click on the Connect button, select Connect to local runtime, and follow the instructions to enter the local server's port (usually 8888).

