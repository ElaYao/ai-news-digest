# AI News Digest

**AI News Digest** is an automated system designed to collect, process, and summarize the latest news in the AI industries. This project integrates web scraping, data preprocessing, machine translation, and AI-driven text summarization to provide concise, accurate, and timely news reports.

## 📌 Project Overview

The objective of AI News Digest is to streamline the process of gathering industry-related information, enabling users to stay informed about key developments in the rapidly evolving fields of Web3 and AI. The system automatically scrapes news articles from designated sources, filters relevant content, translates headlines, generates AI-powered summaries, and compiles the information into structured reports.

## ⚙️ Key Features

1. **Automated Web Scraping**  
   - Efficient extraction of news articles from targeted websites using `BeautifulSoup` and `requests`.

2. **Content Filtering and Preprocessing**  
   - Keyword-based filtering to ensure the relevance of collected articles.

3. **Machine Translation**  
   - Integration with `deep-translator` for accurate translation of news headlines into Chinese.

4. **AI-Powered Summarization**  
   - Utilization of OpenAI's GPT-3.5 model to generate concise, coherent summaries suitable for quick consumption.

5. **Automated Report Generation**  
   - Conversion of processed data into a well-structured HTML report for easy access and readability.

## 🗂️ Project Structure

```
ai-news-digest/
├── data/                   # Storage for raw and processed data
│   └── summarized_news.csv # Final processed news data
├── src/                    # Source code containing core modules
│   ├── scraper.py          # Handles web scraping from news sources
│   ├── translator.py       # Translates news headlines to Chinese
│   ├── summarizer.py       # Generates summaries using AI models
│   └── report_generator.py # Compiles data into an HTML report
├── main.py                 # Entry point for executing the project
├── requirements.txt        # Python dependencies for the project
├── .gitignore              # Specifies files/folders to be ignored by Git
├── .env                    # Environment variables (e.g., API keys)
└── README.md               # Project documentation
```
   

## 🚀 Getting Started

### 1️ Clone the Repository

```bash
git clone https://github.com/ElaYao/ai-news-digest.git
cd ai-news-digest
```

### 2 Install Dependencies
```bash
pip install -r requirements.txt
```

### 3 Set Up Environment Variables
Create a .env file to securely store API credentials:
```bash
OPENAI_API_KEY=your_openai_api_key
```

### 4 Run the Application
```bash
python main.py
```

This will:

- Scrape the latest news articles
- Filter relevant content  
- Translate headlines  
- Generate AI-based summaries  
- Produce an HTML report (news.html)  

## 📊 Dependencies
- pandas - Data manipulation and analysis
- requests & BeautifulSoup - Web scraping
- deep-translator - Machine translation
- openai - AI-driven summarization
- dotenv - Environment variable management

To install all dependencies:
```bash
pip install -r requirements.txt
```

## 📈 Potential Improvements
1. Integration with additional news sources and APIs
2. Advanced sentiment analysis for market trends
3. Real-time monitoring and notification features


