# basic example code 2
import chromadb

client = chromadb.Client()

collection = client.create_collection(name="my_doc1")

collection.add(
    documents=[
        "ChromaDB is a vector database",
        "LangChain helps build LLM apps",
        "Agents need memory"
    ],
    ids=["doc1","doc2","doc3"]
)

results = collection.query(
    query_texts=["What is ChromaDB?"],
    n_results=1
)


print(results["documents"])


