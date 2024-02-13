import os
from resp.apis.arxiv_api import Arxiv

ap = Arxiv()
q = 'Zero-shot learning'
arxiv_result = ap.arxiv(q, max_pages = 1)

print(arxiv_result)

urls = []

for link in arxiv_result.link:
    url = link[:18] + 'pdf' + link[21:] + '.pdf'
    urls.append(url)

for url in urls[:5]:
    os.system('wget ' + url)

def get_scientific_papers(q):
    arxiv_result = ap.arxiv(q, max_pages = 1)
    for link in arxiv_result.link:
        url = link[:18] + 'pdf' + link[21:] + '.pdf'
        urls.append(url)

    for url in urls[:5]:
        os.system('wget ' + url)