import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
# Replace 'kddcup.data' with the correct path to your dataset
data = pd.read_csv("G:/Train Ai Data/kddcup.data", header=None)

# Add column names (optional but recommended)
columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"
]
data.columns = columns

# Preprocessing
# 1. Encode categorical features (e.g., protocol_type, service, flag)
data = pd.get_dummies(data, columns=["protocol_type", "service", "flag"])

# 2. Separate features and labels
X = data.drop("label", axis=1)  # Features
y = data["label"]  # Labels

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Save the preprocessed data
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Preprocessed data saved as X_train.csv, X_test.csv, y_train.csv, and y_test.csv")