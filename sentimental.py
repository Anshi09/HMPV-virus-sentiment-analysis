import pandas as pd
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# Load data
df = pd.read_csv("hmpv_news.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score < 0.1:
        return "Happy 😊"
    elif score > 0.5:
        return "Angry 😡"
    elif 0.1>= score <= 0.3:
        return "Sad 😢"
    elif 0.3>=score <=0.5:
        return "Shocked 😲"

df["Sentiment"] = df["Title"].apply(get_sentiment)
df.to_csv("hmpv_news_with_sentiment.csv", index=False)
print("Sentiment analysis completed.")
