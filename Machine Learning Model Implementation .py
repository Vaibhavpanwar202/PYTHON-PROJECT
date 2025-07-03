#sample_data.csv
age,sex,cp,trestbps,chol,fbs,restecg,thalach,target
63,1,3,145,233,1,0,150,1
37,1,2,130,250,0,1,187,1
41,0,1,130,204,0,0,172,1
56,1,1,120,236,0,1,178,1
57,0,0,120,354,0,1,163,1
57,1,0,140,192,0,1,148,0
56,0,1,140,294,0,0,153,0
44,1,1,120,263,0,1,173,0
52,1,2,172,199,1,1,162,1
57,1,2,150,168,0,1,174,0


# code 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load CSV data
data = pd.read_csv("sample_data.csv")

# Split into features and target
X = data.drop("target", axis=1)
y = data["target"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
