# stability ai 
PS C:\Users\hari_> docker pull ghcr.io/ai-dock/stable-diffusion-webui:v2-rocm-6.0-core-22.04
v2-rocm-6.0-core-22.04: Pulling from ai-dock/stable-diffusion-webui

PS C:\Users\hari_> docker run -d --name stable-diffusion-webui  --gpus all   -p 7860:7860   -v stabilityai:/data   ghcr.io/ai-dock/stable-diffusion-webui:v2-rocm-6.0-core-22.04


PS C:\Users\hari_> docker run -d -p 7860:7860  --gpus all      -v stabilityai:/data   --name stable-diffusion-webui  ghcr.io/ai-dock/stable-diffusion-webui:v2-rocm-6.0-core-22.04
