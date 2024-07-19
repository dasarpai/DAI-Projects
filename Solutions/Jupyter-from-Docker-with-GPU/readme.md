# First run this command 
docker build -t my-jupyter-notebook .

# Second run this command

docker run -it --rm --gpus all -p 8888:8888 -v "$(pwd):/workspace" my-jupyter-notebook

It will launch jupyter in docker and make the link available on the host machine at
http://127.0.0.1:8888/tree

# Then go to Visual code.
ctrl+shift+p 
select kernel 
existing jypter server 
