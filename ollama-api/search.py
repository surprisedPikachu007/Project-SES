from duckduckgo_search import DDGS


def search(query):
    with DDGS() as ddgs:
        return ddgs.text(query, region="in", safesearch="off", timelimit='y', max_results=10)


for r in search("python"):
    print(r)
