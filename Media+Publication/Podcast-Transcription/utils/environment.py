from dotenv import load_dotenv
import os
def load_env():
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
return groq_api_key, pinecone_api_key
