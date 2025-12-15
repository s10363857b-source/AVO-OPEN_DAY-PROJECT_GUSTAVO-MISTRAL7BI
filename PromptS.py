from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """Rispondi SOLO usando il contesto fornito.
Se la risposta non è nel contesto, rispondi: "Non ho informazioni disponibili."

Contesto:
{context}

Domanda:
{question}

Risposta:
"""
)
