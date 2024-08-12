from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_pinecone import PineconeVectorStore
def store_documents_in_pinecone(documents, index_name):
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
docsearch = PineconeVectorStore.from_documents(documents, embedding_function, index_name=index_name)
return docsearch
