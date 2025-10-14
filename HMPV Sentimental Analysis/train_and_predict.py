# train_and_predict.py
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
from scrape_and_preprocess import preprocess_text  # Import the function

# Load or create labeled data
# Replace this with your actual labeled data
data = {
    "text": [
        "HMPV outbreak causes concern among health officials",
        "New vaccine for HMPV shows promising results",
        "HMPV cases decline due to effective public health measures",
        "HMPV spreads rapidly in crowded areas",
    ],
    "label": [0, 1, 1, 0]  # 0 = Negative, 1 = Positive
}
df = pd.DataFrame(data)

# Preprocess the text data
df['cleaned_text'] = df['text'].apply(preprocess_text)

# Feature extraction
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['cleaned_text']).toarray()
y = df['label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model and vectorizer
joblib.dump(model, 'models/hmpv_sentiment_model.pkl')
joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')

# Predict sentiment on new data
def predict_sentiment(new_headlines):
    """
    Predict sentiment for new headlines.
    """
    # Create the 'models' directory if it doesn't exist
os.makedirs('models', exist_ok=True)
    # Load the model and vectorizer
    model = joblib.load('models/hmpv_sentiment_model.pkl')
    vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
    
    # Preprocess and predict
    cleaned_headlines = [preprocess_text(headline) for headline in new_headlines]
    X_new = vectorizer.transform(cleaned_headlines)
    predictions = model.predict(X_new)
    
    return predictions

# Example usage
if __name__ == "__main__":
    # Scrape new headlines
    url = "https://example-news-website.com/new-hmpv-news"
    new_headlines = scrape_and_preprocess(url)
    
    # Predict sentiment
    predictions = predict_sentiment(new_headlines)
    for headline, sentiment in zip(new_headlines, predictions):
        print(f"Headline: {headline} | Sentiment: {'Positive' if sentiment == 1 else 'Negative'}")