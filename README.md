# HMPV Virus Sentiment Analysis

A Python-based sentiment analysis application that analyzes text related to Human Metapneumovirus (HMPV) and classifies the sentiment. The project includes a Flask backend, TextBlob-based sentiment scoring, CSV storage, and a simple web interface.

## Overview

This project explores how sentiment analysis can be applied to public reactions and news-related text about HMPV. Users can submit text through the web application, receive a sentiment classification, and store analyzed inputs for later inspection.

## Features

- Flask web application
- Text sentiment analysis using TextBlob
- Input text preprocessing and sanitization
- REST-style `/analyze` endpoint
- CSV-based storage of analyzed text
- JSON response support
- CORS enabled for frontend integration
- Simple browser-based interface

## Tech Stack

- **Python**
- **Flask**
- **TextBlob**
- **Pandas**
- **Flask-CORS**
- **HTML/CSS/JavaScript**

## Project Structure

```text
HMPV-virus-sentiment-analysis/
├── app.py
├── templates/
│   └── sample.html
├── usersearch/
│   └── input.csv
├── README.md
└── ...
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Anshi09/HMPV-virus-sentiment-analysis.git
cd HMPV-virus-sentiment-analysis
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask flask-cors textblob pandas
```

### 4. Run the application

```bash
python app.py
```

Open the local address shown by Flask in your browser.

## API Endpoint

The application exposes:

```text
POST /analyze
```

Example form field:

```text
text=Your text about HMPV goes here
```

The endpoint returns a JSON response containing the analyzed data.

## What I Learned

This project demonstrates practical experience with:

- Building a Python web application with Flask
- Integrating a natural-language processing library
- Cleaning and validating user input
- Designing a simple API endpoint
- Persisting application data with Pandas/CSV
- Connecting a frontend interface to a Python backend

## Future Improvements

- Replace rule-based sentiment categorization with a trained ML classifier
- Add a larger labeled HMPV sentiment dataset
- Add sentiment visualizations and analytics
- Improve multilingual text handling
- Add automated tests
- Deploy the application using a cloud platform

## Author

**Anshika Rana**  
M.Tech Computer Science & Engineering

- GitHub: https://github.com/Anshi09
