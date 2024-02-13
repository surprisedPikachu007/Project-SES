from langchain_community.llms.ollama import Ollama
from articles import get_pages

llm = Ollama(model="mistral-openorca:latest")

pages = get_pages()

for page in pages:
    print(llm.invoke(page))
    print("-------------------------------------------------")
    