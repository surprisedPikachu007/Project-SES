import requests
import urllib.parse as urlparse

params = {
    "key": "AIzaSyBa5Zc_DZ_9KGKffMu73a5En3vVTHC7z6w",
    "cx": "8238a86e200a44222",
    "q": "cricket news today site:indianexpress.com",
    "start": 0
}

base_url = "https://www.googleapis.com/customsearch/v1"

url_parts = list(urlparse.urlparse(base_url))
url_parts[4] = urlparse.urlencode(params)

gcse_url = urlparse.urlunparse(url_parts)
data = requests.get(gcse_url).json()
items = data["items"]

with open("data2.json", "w") as f:
    f.write(str(data))
