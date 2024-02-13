from search_engine_parser.core.engines.googlenews import Search as GoogleNewsSearch
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.duckduckgo import Search as DuckDuckGoSearch

search_engine_priority_list = [GoogleNewsSearch, GoogleSearch, BingSearch, DuckDuckGoSearch]
news_sites = ['indianexpress.com', 'thehindu.com', 'timesofindia.indiatimes.com', 'hindustantimes.com', 'ndtv.com']


def get_article_links(q):
    query = q + ' news' + ' site:' + ' OR site:'.join(news_sites)
    for search_engine in search_engine_priority_list:
        search = search_engine()
        try:
            res = search.search(query, 1)
            links = [r['link'] for r in res]
            return links
        except:
            continue
    return []


print(get_article_links('india'))
