from langchain_community.vectorstores import FAISS

from Project234.Embedding import embeddings
from Project234.doc import documents

vectorstore = FAISS.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
