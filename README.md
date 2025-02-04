# AI News Digest

**AI News Digest** is an automated system designed to collect, process, and summarize the latest news in the Web3 and AI industries. This project integrates web scraping, data preprocessing, machine translation, and AI-driven text summarization to provide concise, accurate, and timely news reports.

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
ai-news-digest/ ├── data/ # Storage for raw and processed data ├── src/ # Source code │ ├── scraper.py # Handles data scraping from news sources │ ├── translator.py # Translates headlines into Chinese │ ├── summarizer.py # Generates summaries using AI models │ └── report_generator.py # Compiles data into an HTML report ├── main.py # Main execution script ├── requirements.txt # List of project dependencies ├── .gitignore # Specifies files and directories to be ignored by Git └── README.md # Project documentation


## 🚀 Getting Started

### 1️ Clone the Repository

git clone https://github.com/ElaYao/ai-news-digest.git
cd ai-news-digest

### 2 Install Dependencies
pip install -r requirements.txt

### 3 Set Up Environment Variables
Create a .env file to securely store API credentials:
OPENAI_API_KEY=your_openai_api_key

### 4 Run the Application
python main.py
