from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("GRU.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)

split_docs = splitter.split_documents(docs)
print(len(split_docs))

print(split_docs[0].page_content)