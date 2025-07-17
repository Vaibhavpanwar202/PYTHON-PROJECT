# fake_news_detector.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Load the dataset
data = pd.read_csv('fake_or_real_news.csv')  # Make sure to have this CSV
print("Dataset Loaded. Shape:", data.shape)

# Step 2: Split the dataset
X = data['text']  # Features
y = data['label']  # Target (fake or real)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)

# Step 3: Vectorize the text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = vectorizer.fit_transform(X_train)
tfidf_test = vectorizer.transform(X_test)

# Step 4: Train the model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(tfidf_train, y_train)

# Step 5: Predict and evaluate
y_pred = model.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f"Accuracy: {round(score * 100, 2)}%")

# Step 6: Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
print("\nConfusion Matrix:\n", conf_matrix)



# fake_or_real_news.csv
# text,label
# "President declares national emergency over health concerns.","REAL"
# "Scientists discover new species of bird in the Amazon rainforest.","REAL"
# "Aliens have landed in Texas, claim local farmers.","FAKE"
# "COVID-19 vaccine causes people to grow extra limbs, say conspiracy theorists.","FAKE"
# "Stock market hits all-time high amid economic recovery.","REAL"
# "Government is replacing drinking water with mind control chemicals.","FAKE"
# "New electric car model can drive 1000 km on a single charge.","REAL"
# "Man travels through time to warn of future apocalypse.","FAKE"
# "Schools to reopen next week with safety measures in place.","REAL"
# "5G towers are spreading the virus, claims viral video.","FAKE"
