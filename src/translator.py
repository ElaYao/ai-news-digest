from deep_translator import GoogleTranslator

df.drop_duplicates(inplace=True)

keywords = ["AI", "Investment", "ML", "Machine Learning", "Elon Musk"]
df = df[df['content'].str.contains('|'.join(keywords),case=False, na=False)]

df.to_csv("cleaned_news.csv", index=False)
print("数据清洗完成，已保存至csv文件！")