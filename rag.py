import sys
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass  # Fallback to default sqlite3 if pysqlite3 isn’t available

from uuid import uuid4
from pathlib import Path
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_chroma import Chroma 
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate




# Constants
CHUNK_SIZE = 1000
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "real_estate"

llm = None
vector_store = None


def initialize_components():
    global llm, vector_store

    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9, max_tokens=500)

    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=ef,
            persist_directory=str(VECTORSTORE_DIR)
        )


def process_urls(urls):
    """
    This function scraps data from a url and stores it in a vector db
    :param urls: input urls
    :return:
    """
    yield "Initializing Components"
    initialize_components()

    yield "Resetting vector store...✅"
    vector_store.reset_collection()

    yield "Loading data...✅"
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    yield "Splitting text into chunks...✅"
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=CHUNK_SIZE
    )
    docs = text_splitter.split_documents(data)

    yield "Add chunks to vector database...✅"
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(
        docs, 
        ids=uuids
    )

    yield "Done adding docs to vector database...✅"

def generate_answer(query):
    if not vector_store:
        raise RuntimeError("Vector database is not initialized")

    # Build the document combination chain (equivalent to what RetrievalQAWithSourcesChain did)
    prompt = ChatPromptTemplate.from_template(
        "Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {input}"
    )
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    # Replace the deprecated chain
    chain = create_retrieval_chain(vector_store.as_retriever(), combine_docs_chain)

    result = chain.invoke({"input": query})
    answer = result.get("answer", result.get("output_text", ""))
    # Extract sources as a list of strings (URLs or 'Unknown')
    sources_list = [doc.metadata.get("source", "Unknown") for doc in result.get("context", [])]
    # Return only the first source, or 'Unknown' if none
    source = sources_list[0] if sources_list else "Unknown"
    return answer, source

    # ...existing code...

