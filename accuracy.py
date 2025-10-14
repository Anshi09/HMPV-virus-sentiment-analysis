import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load CSV
df = pd.read_csv("hmpv_sentiment_sample.csv")

# 2. Encode labels
label_map = {'Happy': 0, 'Sad': 1, 'Shocked': 2, 'Angry': 3}
reverse_map = {v: k for k, v in label_map.items()}
df['label'] = df['Sentiment'].map(label_map)

# 3. Train-test splitcognIDE
X_train, X_test, y_train, y_test = train_test_split(df['Tweet'], df['label'], test_size=0.2, random_state=42)

# 4. TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train model
model = LogisticRegression(max_iter=200, class_weight='balanced')
model.fit(X_train_vec, y_train)

# 6. Predict
y_pred = model.predict(X_test_vec)

# Debugging: Print unique labels in y_test and y_pred
print("Unique labels in y_test:", sorted(set(y_test)))
print("Unique labels in y_pred:", sorted(set(y_pred)))

# 7. Evaluation
print("Classification Report:\n")
print(classification_report(
    y_test, 
    y_pred, 
    labels=list(label_map.values()),  # Use all labels from label_map
    target_names=list(label_map.keys())  # Match target names to all labels
))

# 8. Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=list(label_map.values()))  # Use all labels from label_map
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=list(label_map.keys()),  # Use all labels from label_map
            yticklabels=list(label_map.keys()))  # Use all labels from label_map
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()
