# scrape_and_preprocess.py
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def scrape_news(url):
    """
    Scrape news headlines from a given URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract headlines (adjust the selector based on the website structure)
    headlines = []
    for item in soup.find_all('h2', class_='headline-class'):  # Update selector
        headlines.append(item.get_text())
    
    return headlines

def preprocess_text(text):
    """
    Preprocess text by cleaning, tokenizing, and removing stopwords.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(tokens)

def scrape_and_preprocess(url):
    """
    Scrape headlines and preprocess them.
    """
    headlines = scrape_news(url)
    cleaned_headlines = [preprocess_text(headline) for headline in headlines]
    return cleaned_headlines

# Example usage
if __name__ == "__main__":
    url = "https://example-news-website.com/hmpv-news"
    cleaned_headlines = scrape_and_preprocess(url)
    print(cleaned_headlines)