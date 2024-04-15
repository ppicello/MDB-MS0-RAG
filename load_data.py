from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import PyPDFLoader
import key_param
import os.path
from os import path

# Set the MongoDB URI, DB, Collection Names
client = MongoClient(key_param.MONGO_URI)
dbName = key_param.MONGO_DB
collectionName = key_param.MONGO_COLL
collection = client[dbName][collectionName]

## INDEX TXT FILES

# Initialize the DirectoryLoader
loader = DirectoryLoader( './sample_files', glob="./*.txt", show_progress=True)
data = loader.load()

# Define the OpenAI Embedding Model we want to use for the source data
embeddings = OpenAIEmbeddings(openai_api_key=key_param.openai_api_key, model="text-embedding-ada-002")

# Initialize the VectorStore, and vectorise the text from the documents using the specified embedding model, and insert them into the specified MongoDB collection
vectorStore = MongoDBAtlasVectorSearch.from_documents( data, embeddings, collection=collection )

print('Computed embeddings for TXT files')

## INDEX PDF FILES - chunking by page

chunked_docs = {}

# Loop thorugh the different files and split them into chunks (by page)
for filename in os.listdir('./sample_files'):
  if filename.endswith('pdf'):
      print(filename)
      loader = PyPDFLoader(os.path.join('./sample_files', filename))
      chunked_docs[filename] = loader.load_and_split()
      print('computed ' + str(len(chunked_docs[filename])) + ' chunks for document: ' + filename)


# Generate vectors for each chunk
for key,value in chunked_docs.items():
  print('Computing vectors for document: ' + key)
  vector_db = MongoDBAtlasVectorSearch.from_documents(
    value,
    embeddings,
    collection=collection
)

print('Computed embeddings for PDF files')

