from Project234.RAGC import rag_chain

query = "Ma...quando apre la segreteria?"

result = rag_chain.invoke(query)
print(result)
