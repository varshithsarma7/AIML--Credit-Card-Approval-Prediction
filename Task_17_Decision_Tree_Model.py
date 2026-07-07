# ============================================================
# Task 17 : Decision Tree Model
# Credit Card Approval Prediction System
# ============================================================

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------------------------------------
# Read Datasets
# ------------------------------------------------------------

application = pd.read_csv("Dataset/application_record.csv")
credit = pd.read_csv("Dataset/credit_record.csv")

# ------------------------------------------------------------
# Create Target Variable
# ------------------------------------------------------------

credit["TARGET"] = credit["STATUS"].apply(
    lambda x: 1 if x in ["2", "3", "4", "5"] else 0
)

target = credit.groupby("ID")["TARGET"].max().reset_index()

# ------------------------------------------------------------
# Merge Datasets
# ------------------------------------------------------------

df = application.merge(target, on="ID", how="inner")

# ------------------------------------------------------------
# Handle Missing Values
# ------------------------------------------------------------

for col in df.select_dtypes(include="object").columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# ------------------------------------------------------------
# Encode Categorical Values
# ------------------------------------------------------------

encoder = LabelEncoder()

for col in df.select_dtypes(include="object").columns:
    df[col] = encoder.fit_transform(df[col])

# ------------------------------------------------------------
# Features and Target
# ------------------------------------------------------------

X = df.drop(["ID", "TARGET"], axis=1)
y = df["TARGET"]

# ------------------------------------------------------------
# Train Test Split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------------------------------------------
# Decision Tree Model
# ------------------------------------------------------------

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# ------------------------------------------------------------
# Prediction
# ------------------------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------------------------
# Evaluation
# ------------------------------------------------------------

print("\nAccuracy Score")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nTask 17 Completed Successfully!")
