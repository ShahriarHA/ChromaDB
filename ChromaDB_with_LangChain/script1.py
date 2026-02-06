# ChromaDB with LangChain
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorStore = Chroma(
    collection_name="agent_knowledge",
    embedding_function=embeddings,
    persist_directory="./ChromaDB_with_LangChain/my_ChromaDB"
)

vectorStore.add_texts(
    texts=[
        "Agentic AI needs long-term memory",
        "ChromaDB stores vector embeddings",
        "Ollama runs models locally"
    ],
    ids=["d1","d2","d3"]
)

docs = vectorStore.similarity_search(
    "How do agents remember things?",
    k=2
)

for doc in docs:
    print(doc.page_content)




