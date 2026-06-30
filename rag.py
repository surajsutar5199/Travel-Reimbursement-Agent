# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings

# # Load Policy File
# loader = TextLoader("data/policy.txt")
# documents = loader.load()

# # Split into Chunks
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# docs = text_splitter.split_documents(documents)

# # Create Embeddings
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # Create FAISS Index
# vector_db = FAISS.from_documents(docs, embeddings)

# # Create Retriever
# retriever = vector_db.as_retriever(search_kwargs={"k": 2})


