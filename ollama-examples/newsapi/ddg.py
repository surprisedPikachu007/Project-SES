from newsapi import NewsApiClient
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.llms import Ollama

llm = Ollama(model="summistral")

newsapi = NewsApiClient(api_key='5707e0ccd82c4f92bdfbdbc731f574e8')

url = 'https%3A%2F%2Fwww.thehindu.com%2F&rut=491a2ae717625128c34e3dc1404f2efdb6b9bd47dd17c976a25500a40a5e92ee'
url = 'https://www.thehindu.com'

loader = WebBaseLoader(url)
docs = loader.load()
page_content = docs[0].page_content

for token in llm.stream(page_content):
    print(token, end='')
