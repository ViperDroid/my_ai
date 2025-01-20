import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
data = pd.read_csv("kddcup.data.csv")

# Preprocessing
# 1. Encode categorical features (e.g., protocol_type, service, flag)
data = pd.get_dummies(data, columns=["protocol_type", "service", "flag"])

# 2. Separate features and labels
X = data.drop("label", axis=1)  # Features
y = data["label"]  # Labels

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Save the model
joblib.dump(model, "intrusion_detection_model.pkl")
print("Model saved as 'intrusion_detection_model.pkl'")