from newsapi import NewsApiClient
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.llms import Ollama

llm = Ollama(model="summistral")

newsapi = NewsApiClient(api_key='5707e0ccd82c4f92bdfbdbc731f574e8')

query = st.text_input("Search query")
if query:
    all_articles = newsapi.get_everything(q=query, page_size=5, sort_by='publishedAt')
    urls = [article['url'] for article in all_articles['articles']]
    for article in all_articles['articles']:
        loader = WebBaseLoader(article['url'])
        docs = loader.load()
        page_content = docs[0].page_content
        st.write(page_content)
        st.subheader("Summary")
        # summary = llm.invoke(page_content)
        for token in llm.stream(page_content):
            st.write(token)
            print(token, end='')
        st.write("--------------------------------------------")
