from audio_processing.audio_to_text import audio_to_text
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
import pandas as pd
import numpy as np
def transcribe_podcasts(episodes_df, text_splitter):
documents = []
cnt = 0
for index, row in episodes_df.iterrows():
cnt += 1
audio_filepath = row['filepath']
transcript = audio_to_text(audio_filepath)
chunks = text_splitter.split_text(transcript)
for chunk in chunks:
header = f"Date: {row['published_date']}\nEpisode Title: {row['title']}\n\n"
documents.append(Document(page_content=header + chunk, metadata={"source": "local"}))
if np.mod(cnt, round(len(episodes_df) / 5)) == 0:
print(round(cnt / len(episodes_df), 2) * 100, '% of transcripts processed...')
return documents
