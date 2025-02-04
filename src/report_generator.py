import pandas as pd

def generate_html_report(df, output_path="news.html"):
    html_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>每日AI新闻摘要</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f8f9fa; }
        .container { max-width: 800px; margin: 30px auto; background: white; padding: 20px; border-radius: 10px; }
        h1 { text-align: center; }
        .news-item { padding: 15px; border-bottom: 1px solid #ddd; }
        .news-title { font-size: 18px; font-weight: bold; color: #007bff; }
        .news-summary { font-size: 14px; color: #555; }
    </style>
</head>
<body>
    <div class="container">
        <h1>每日AI新闻摘要</h1>
'''
    for _, row in df.iterrows():
        html_content += f'''
        <div class="news-item">
            <div class="news-title">{row['title_cn']}</div>
            <div class="news-summary">{row['Summary']}</div>
        </div>
        '''
    html_content += '</div></body></html>'

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"✅ HTML 生成成功！请打开 `{output_path}` 查看新闻页面。")
