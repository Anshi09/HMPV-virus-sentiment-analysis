from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
import pandas as pd
import os
import re

app = Flask(__name__)
CORS(app)

# Ensure 'usersearch' directory exists
if not os.path.exists("usersearch"):
    os.makedirs("usersearch")

@app.route('/')
def index():
    return render_template('sample.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.form.get('text', '').strip()
        print("Received text:", text)
        if not text:
            return jsonify({'error': 'Please enter some text to analyze.'}), 400

        text = re.sub(r'[^\x00-\x7F]+', '', text)
        text = re.sub(r'\s+', ' ', text)
        print("Sanitized text:", text)

        try:
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            print("Sentiment score:", sentiment_score)
        except Exception as e:
            print("Tokenization error:", str(e))
            return jsonify({'error': f'Tokenization error: {str(e)}'}), 500

        if  0.1 > sentiment_score:
            sentiment_category = "Happy 😊"
        elif 0.3> sentiment_score > 0.5 :
            sentiment_category = "Angry 😡"
        elif  0.5 > sentiment_score :
            sentiment_category = "Sad 😢"
        elif 0.1>sentiment_score > 0.3:
            sentiment_category = "Shocked 😲"
        else:
            sentiment_category="Neutral 😐"
           
            print("Category:", sentiment_category)

        csv_file = "usersearch/input.csv"
        data = {'Text': [text], 'Sentiment': [sentiment_category]}
        df = pd.DataFrame(data)
        if os.path.exists(csv_file):
            df.to_csv(csv_file, mode='a', header=False, index=False)
        else:
            df.to_csv(csv_file, index=False)

        print("Saved to CSV.")

        df = pd.read_csv(csv_file)
        json_data = df.to_json(orient='records', indent=4)
        print("Returning JSON.")

        return jsonify({'data': json_data})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
