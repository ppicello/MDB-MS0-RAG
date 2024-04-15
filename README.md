# Atlas Vector Search MS0

This repo is the template for the MongoDB Atlas Vector Search MS0 workshop. This example is using MongoDB Atlas as vector database, OpenAI as embedding model and LLM and LangChain as LLM framework.

In this example we are using TXT and PDF files.

## Setting up the Environment

1. Install the dependencies:
```
pip install -r requirements.txt
```
2. Create OpenAI API Key from [here](https://platform.openai.com/account/api-keys). Note that this requires a paid account with OpenAI, with enough credits. 

4. Create a MongoDB Atlas cluster and set up the required vector search index.

4. Save the OpenAI API key and the MongoDB URI in the `key_param.py` file, like this:
```
openai_api_key = "ENTER_OPENAI_API_KEY_HERE"
MONGO_URI = "ENTER_MONGODB_URI_HERE"
MONGO_DB = "ENTER_MONGODB_DB_NAME_HERE"
MONGO_COLL = "ENTER_MONGODB_COLLECTION_NAME_HERE"
```

5. Use the following two python scripts:
   - **load_data.py**: This script will be used to load your documents and ingest the text and vector embeddings, in a MongoDB collection.
   - **rag.py**: This script will generate the user interface and will allow you to perform question-answering against your data, using Atlas Vector Search and OpenAI.

