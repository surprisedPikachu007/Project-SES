from fastapi import FastAPI
from summarizer import summarize as sum, summarize_custom

app = FastAPI()


@app.get("/")
async def root():
    return "API is running"


@app.get("/summarize")
def summarize(text: str, max_length: int = None):
    if max_length:
        return summarize_custom(text, max_length)
    return sum(text)
