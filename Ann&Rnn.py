import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SimpleRNN, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# 1. Load CSV
df = pd.read_csv("hmpv_sentiment_dataset_project.csv")

# 2. Encode labels
label_map = {'Happy': 0, 'Sad': 1, 'Shocked': 2, 'Angry': 3}
reverse_map = {v: k for k, v in label_map.items()}
df['label'] = df['Sentiment'].map(label_map)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(df['Tweet'], df['label'], test_size=0.2, random_state=42)

# 4. Tokenization and Padding
tokenizer = Tokenizer(num_words=5000)  # Use the top 5000 words
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

max_len = 100  # Maximum length of sequences
X_train_pad = pad_sequences(X_train_seq, maxlen=max_len, padding='post')
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len, padding='post')

# One-hot encode labels
y_train_cat = to_categorical(y_train, num_classes=len(label_map))
y_test_cat = to_categorical(y_test, num_classes=len(label_map))

# 5. ANN Model
def build_ann(input_dim):
    model = Sequential()
    model.add(Dense(128, activation='relu', input_dim=input_dim))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(len(label_map), activation='softmax'))  # Output layer
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Train ANN
print("Training ANN...")
ann_model = build_ann(X_train_pad.shape[1])
ann_history = ann_model.fit(X_train_pad, y_train_cat, epochs=10, batch_size=32, validation_data=(X_test_pad, y_test_cat))

# 6. RNN Model
def build_rnn(vocab_size, max_len):
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=128, input_length=max_len))
    model.add(SimpleRNN(128, return_sequences=False))
    model.add(Dense(len(label_map), activation='softmax'))  # Output layer
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Train RNN
print("Training RNN...")
rnn_model = build_rnn(vocab_size=5000, max_len=max_len)
rnn_history = rnn_model.fit(X_train_pad, y_train_cat, epochs=10, batch_size=32, validation_data=(X_test_pad, y_test_cat))

# 7. Evaluation
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    y_pred_labels = y_pred.argmax(axis=1)
    print(f"\nClassification Report for {model_name}:\n")
    print(classification_report(y_test, y_pred_labels, target_names=list(label_map.keys())))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred_labels)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=list(label_map.keys()),
                yticklabels=list(label_map.keys()))
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()

# Evaluate ANN
evaluate_model(ann_model, X_test_pad, y_test, "ANN")

# Evaluate RNN
evaluate_model(rnn_model, X_test_pad, y_test, "RNN")