# ============================================================
# Task 14 : Handling Categorical Values
# Credit Card Approval Prediction System
# ============================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ------------------------------------------------------------
# Read Dataset
# ------------------------------------------------------------

app = pd.read_csv("Dataset/application_record.csv")

# ------------------------------------------------------------
# Fill Missing Values
# ------------------------------------------------------------

for column in app.select_dtypes(include=['object']).columns:
    app[column].fillna(app[column].mode()[0], inplace=True)

# ------------------------------------------------------------
# Encode Categorical Columns
# ------------------------------------------------------------

label_encoder = LabelEncoder()

categorical_columns = app.select_dtypes(include=['object']).columns

for column in categorical_columns:
    app[column] = label_encoder.fit_transform(app[column])

# ------------------------------------------------------------
# Display Encoded Dataset
# ------------------------------------------------------------

print("\nEncoded Dataset (First Five Rows):")
print(app.head())

print("\nEncoded Categorical Columns:")
print(categorical_columns)

print("\nTask 14 Completed Successfully!")
