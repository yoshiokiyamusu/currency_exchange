# REST Api: https://www.youtube.com/watch?v=0w5BLvb9-mA

import requests
url_api ='https://newsapi.org/v2/everything?qInTitle=stock%20market&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'
r = requests.get(url_api)
content = r.json()
#print(content['articles'][0]['author'])

results = []
# Slicing the list to get only the first 20 items
for article in content['articles'][:3]:
    results.append(f"Title:' {article['title']},'\nURL: '{article['url']}")
    print(results)


