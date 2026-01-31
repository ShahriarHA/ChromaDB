# Basic ChromaDB Example code
import chromadb

# Create a Chroma client
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="my_chromaDB")

# Add documents
collection.add(
    documents=[
        "ChromaDB is a vector database",
        "LangChain helps build LLM apps",
        "Agents need memory"
    ],
    ids=["doc1", "doc2", "doc3"]
)

# Query by meaning
results = collection.query(
    query_texts=["What do agents use for memory?"],
    n_results=2
)
print(results["documents"])


