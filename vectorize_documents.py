from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# loaidng the embedding model
embeddings = HuggingFaceEmbeddings()

loader = DirectoryLoader(path="data",
                         glob="./*.pdf",
                         loader_cls=PyPDFLoader)
documents = loader.load()


text_splitter = CharacterTextSplitter(chunk_size=2000,
                                      chunk_overlap=500)
text_chunks = text_splitter.split_documents(documents)

vectordb = Chroma.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    persist_directory="vector_db_dir"
)

print("Documents Vectorized")