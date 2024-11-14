import os
import streamlit as st
import pandas as pd
from embeddings.vector_store import store_documents_in_pinecone
from transcriptions.transcribe_podcasts import transcribe_podcasts
from utils.environment import load_env
from langchain_groq.chat_completion import transcript_chat_completion
# Load environment variables
groq_api_key, pinecone_api_key = load_env()
st.title("Podcast Content Query App")
st.write("Ask questions based on the content of the podcast.")
# Load episode metadata
episode_metadata_df = pd.read_csv('data/episode_metadata.csv')
chunk_fps = os.listdir('data/mp3-chunks/')
episode_chunk_df = pd.DataFrame({
'filepath': [f"data/mp3-chunks/{fp}" for fp in chunk_fps],
'episode_id': [fp.split('_chunk')[0] for fp in chunk_fps]
})
episodes_df = episode_chunk_df.merge(episode_metadata_df, on='episode_id')
# Transcribe podcasts
text_splitter = TokenTextSplitter(chunk_size=500, chunk_overlap=20)
documents = transcribe_podcasts(episodes_df, text_splitter)
# Store documents in Pinecone
pinecone_index_name = "podcast-transcripts"
docsearch = store_documents_in_pinecone(documents, pinecone_index_name)
# Handle user input
user_question = st.text_input("Enter your question:", "")
if user_question:
    with st.spinner("Querying..."):
    relevent_docs = docsearch.similarity_search(user_question)
    relevant_transcripts = '\n\n------------------------------------------------------\n\n'.join([doc.page_content for doc in relevent_docs[:3]])
    response = transcript_chat_completion(groq_api_key, relevant_transcripts, user_question)
    st.write("**Answer:**", response)
