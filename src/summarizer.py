import openai

api_key = "your_openai_api_key"
client = openai.Client(api_key=api_key)

def summarize_news(content):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"请用一段中文总结这篇新闻的内容，并以较高的可读性呈现给中文读者阅读，全文不超过250字。：{content}"}
        ]
    )
    return response.choices[0].message.content