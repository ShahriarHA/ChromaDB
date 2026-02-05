# add embeddings properly
import chromadb
from chromadb.utils import embedding_functions

embeddingFunction = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()

collection = client.create_collection(name="my_doc3")

collection.add(
    documents=[
        "ChromaDB is a vector database",
        "LangChain helps build LLM apps",
        "Agents need memory"
    ],
    ids=["d1","d2","d3"]
)

res = collection.query(
    query_texts=["What is ChromaDB?"],
    n_results=1
)

print(res["documents"])


