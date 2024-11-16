Readme by Hari Thapliyal

## Steps

- WSL
- jupyter-notebook --no-browser --port=8888 --ip=0.0.0.0
	- It will create one url
- Open notebook in colab 
- Use the generated url to connect 

- $ docker run --runtime=nvidia -it --rm -p 8081:8081 -v "$PWD":/opt/colab -v $HOME/.cache/torch:/root/.cache/torch sorokine/docker-colab-local:10.1
