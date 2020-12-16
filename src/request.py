import requests

response = requests.get("https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.10.5.json")

data = response.json()

# for news in data['articleList']:
#     print(news['url'])
data['articleList']