from fastapi import FastAPI
from news import get_article_links


app = FastAPI()


@app.get("/")
def root():
    return "usage: /search?q=your_query_here"


@app.get("/search")
def search(q: str):
    return get_article_links(q)
