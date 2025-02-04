import pandas as pd
from src.scraper import fetch_news, extract_article_content
from src.translator import translate_text
from src.summarizer import summarize_news
from src.report_generator import generate_html_report

if __name__ == "__main__":
    url = "http://venturebeat.com/category/ai/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    # Step 1: 抓取新闻
    news_list = fetch_news(url, headers)
    all_articles = []
    for title, link in news_list[:10]:
        content = extract_article_content(link)
        all_articles.append({"title": title, "url": link, "content": content})

    df = pd.DataFrame(all_articles)
    df.drop_duplicates(inplace=True)

    # Step 2: 关键词筛选
    keywords = ["AI", "Investment", "ML", "Machine Learning", "Elon Musk"]
    df = df[df['content'].str.contains('|'.join(keywords), case=False, na=False)]

    # Step 3: 翻译标题
    df['title_cn'] = df['title'].apply(translate_text)

    # Step 4: 生成摘要
    df['Summary'] = df['content'].apply(summarize_news)

    # Step 5: 保存和生成报告
    df.to_csv("data/summarized_news.csv", index=False)
    generate_html_report(df)

    print("数据处理和报告生成完成！")
