from setuptools import setup, find_packages
setup(
name='podcast_chat_app',
version='0.1',
packages=find_packages(),
install_requires=[
'groq',
'langchain',
'langchain_community',
'langchain_pinecone',
'pydub',
'tiktoken',
'sentence-transformers',
'pinecone_text',
'langchain_groq',
'streamlit',
'python-dotenv',
],
)