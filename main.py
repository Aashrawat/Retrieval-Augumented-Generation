from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = TextLoader("docLoader/notes.txt")
docs = data.load()

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions about the text."),
    ("user", "{data}")
])

model = ChatOpenAI(model="gpt-5-mini")

prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke("prompt")

print(result.content)