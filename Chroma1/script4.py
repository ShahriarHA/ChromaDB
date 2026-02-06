# Persistent Storage (Agent Memory)
import chromadb
from chromadb.utils import embedding_functions

embedding_fun = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
persist_directory = "./my_chromaDB_storage"
chorma_client = chromadb.PersistentClient(path=persist_directory)

collection = chorma_client.get_or_create_collection(name="my_doc5",embedding_function=embedding_fun)

collection.add(
    documents=[
        "ChromaDB is a vector database",
        "LangChain helps build LLM apps",
        "Agents need memory"
    ],
    ids=["d1","d2","d3"]
)

results = collection.query(
    query_texts=["What is ChromaDB?"],
    n_results=1
)

print(results["documents"])



