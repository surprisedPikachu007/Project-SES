from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.ollama import Ollama

loader = PyPDFLoader('/home/aravind-pt7506/college/project/ollama-examples/gcse/scientific papers/papers/2402.00905.pdf')
document = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(document)

embeddings = HuggingFaceEmbeddings()

db = Chroma.from_documents(texts, embeddings)
retriever = db.as_retriever(search_kwargs={'k': 2})

llm = Ollama(model="mistral:7b-instruct-v0.2-q4_0")


