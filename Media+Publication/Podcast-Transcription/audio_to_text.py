import os
from groq import Groq
client = Groq(api_key=os.getenv('GROQ_API_KEY'))
model = 'whisper-large-v3'
def audio_to_text(filepath):
with open(filepath, "rb") as file:
translation = client.audio.translations.create(
file=(filepath, file.read()),
model=model,
)
return translation.text
