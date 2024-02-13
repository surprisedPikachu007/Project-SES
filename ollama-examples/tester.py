from langchain_community.llms.ollama import Ollama
from langchain_community.document_loaders import NewsURLLoader

llm = Ollama(model='mistral-openorca:latest')

urls = [
    'https://www.google.com/url?q=https://indianexpress.com/section/sports/cricket/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAQQAg&usg=AOvVaw0c3RpaMBXSktmqd0wT95P_',
    'https://www.google.com/url?q=https://indianexpress.com/section/sports/cricket/page/3/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAgQAg&usg=AOvVaw2gYqu-8qLe29K14BXz86BH',
    'https://www.google.com/url?q=https://indianexpress.com/about/cricket-news/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAYQAg&usg=AOvVaw3WNAaadjt-KpPcPrDTAnVd',
    'https://indianexpress.com/section/Cricket/page/1686/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAUQAg&usg=AOvVaw2xE64WAcgmvoU0HPpVShZm',
    'https://www.google.com/url?q=https://indianexpress.com/section/Cricket/page/1669/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAcQAg&usg=AOvVaw3V4Yd5ksV8pBxUARJqFRUt',
    'https://www.google.com/url?q=https://indianexpress.com/article/sports/cricket/india-vs-south-africa-live-score-u19-world-cup-2024-semi-final-ind-vs-sa-icc-under-19-wc-latest-scorecard-9146347/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAMQAg&usg=AOvVaw2PZrpisU9NabsArelq1xy1',
    'https://www.google.com/url?q=https://indianexpress.com/section/Cricket/page/1665/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAAQAg&usg=AOvVaw3F2iEZTg5dxT9jwt6eFe5O',
    'https://www.google.com/url?q=https://indianexpress.com/about/indian-cricket-news/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAIQAg&usg=AOvVaw0DfgyQfykRB9LLCy3hEIvb',
    'https://www.google.com/url?q=https://indianexpress.com/section/sports/&sa=U&ved=2ahUKEwj2gZHB7ZqEAxVpyjgGHQO_CR8QFnoECAEQAg&usg=AOvVaw2dbPXNaycIKGIumnJIZks6',
]

loader = NewsURLLoader(urls)
docs = loader.load()
# print(docs)
for doc in docs:
    page_content = doc.page_content

for token in llm.invoke(docs[-1].page_content):
    print(token, end='')