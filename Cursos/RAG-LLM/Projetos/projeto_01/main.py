# Importações básicas
import os

# loader de documentos PDF
from langchain_community.document_loaders import PyPDFLoader

# Divisão de textos em blocos
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embeddings
from langchain_openai import OpenAIEmbeddings

# Banco vetorial
from langchain_community.vectorstores import Chroma

# LLM
from langchain_openai import ChatOpenAI

# Cadeia RAG
# from langchain.chains import RetrievalQA

