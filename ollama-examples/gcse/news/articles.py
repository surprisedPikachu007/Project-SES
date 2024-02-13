from langchain_community.document_loaders import NewsURLLoader
import json

res = json.load(open("/home/aravind-pt7506/college/project/ollama-examples/gcse/news/res.json"))

items = [item for item in res['items']]

links = []
for item in items:
    links.append(item['link'])

loader = NewsURLLoader(links)
docs = loader.load()

pages = [doc.page_content for doc in docs]

def get_pages():
    return pages