docker build -t my-jupyter-notebook .
	
docker run -p 8888:8888 -v ${PWD}:/home/jovyan/work -d my-jupyter-notebook
