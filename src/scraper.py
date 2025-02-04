import requests
from bs4 import BeautifulSoup

def fetch_news(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all("article")
    news_list = []
    for article in articles:
        title_tag = article.find("h2")
        link_tag = article.find("a")
        if title_tag and link_tag:
            title = title_tag.text.strip()
            link = link_tag["href"]
            news_list.append((title, link))
    return news_list

def extract_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    cleaned_paragraphs = paragraphs[1:-10]
    content = "\n".join([p.text.strip() for p in cleaned_paragraphs])
    return content