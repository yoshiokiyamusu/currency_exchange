import requests

def get_news(country, api_key='890603a55bfa47048e4490069ebee18c'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n{article['title']},\nDESCRIPTION\n{article['description']}\n")
    return results

news_list = get_news(country='peru')

# This joins every item in the list with an extra line in between
print("\n---\n".join(news_list))