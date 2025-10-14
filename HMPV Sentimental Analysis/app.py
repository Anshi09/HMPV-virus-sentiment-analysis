import os
from flask import Flask, render_template, request
from scrape_and_preprocess import scrape_and_preprocess
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model_path = 'models/hmpv_sentiment_model.pkl'
vectorizer_path = 'models/tfidf_vectorizer.pkl'

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    raise FileNotFoundError("Model or vectorizer files not found. Please train the model first.")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL from the form
        url = request.form['url']
        
        # Scrape and preprocess headlines
        headlines = scrape_and_preprocess(url)
        
        # Predict sentiment
        X_new = vectorizer.transform(headlines)
        predictions = model.predict(X_new)
        
        # Combine headlines with predictions
        results = []
        for headline, sentiment in zip(headlines, predictions):
            results.append({
                'headline': headline,
                'sentiment': 'Positive' if sentiment == 1 else 'Negative'
            })
        
        return render_template('index.html', results=results)
    
    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)