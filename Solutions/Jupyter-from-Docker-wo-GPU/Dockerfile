FROM jupyter/minimal-notebook:latest

# Install additional packages
RUN pip install numpy pandas matplotlib

# Expose Jupyter port
EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''"]
