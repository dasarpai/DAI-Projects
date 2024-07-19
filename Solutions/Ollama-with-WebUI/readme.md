# ollama : llama3

PS C:\Users\hari_> docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

check: http://localhost:11434/

PS C:\Users\hari_> docker exec -it ollama ollama run llama3
>>> How does transister work?


>>> /bye


# webui 

PS C:\Users\hari_> docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda


PS C:\Users\hari_> docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main