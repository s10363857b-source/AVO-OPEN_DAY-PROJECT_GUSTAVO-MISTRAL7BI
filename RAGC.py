from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from Project234.FAISS import retriever
from Project234.LLMLC import llm
from Project234.PromptS import prompt

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)
