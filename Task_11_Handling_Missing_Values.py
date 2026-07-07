# ============================================================
# Task 11 : Handling Missing Values
# Credit Card Approval Prediction System
# ============================================================

# Import Library
import pandas as pd

# ------------------------------------------------------------
# Read Dataset
# ------------------------------------------------------------

app = pd.read_csv("Dataset/application_record.csv")

# ------------------------------------------------------------
# Check Missing Values
# ------------------------------------------------------------

print("\nMissing Values Before Handling:\n")
print(app.isnull().sum())

# ------------------------------------------------------------
# Fill Missing Numerical Values with Median
# ------------------------------------------------------------

numerical_columns = app.select_dtypes(include=['int64', 'float64']).columns

for column in numerical_columns:
    app[column].fillna(app[column].median(), inplace=True)

# ------------------------------------------------------------
# Fill Missing Categorical Values with Mode
# ------------------------------------------------------------

categorical_columns = app.select_dtypes(include=['object']).columns

for column in categorical_columns:
    app[column].fillna(app[column].mode()[0], inplace=True)

# ------------------------------------------------------------
# Verify Missing Values
# ------------------------------------------------------------

print("\nMissing Values After Handling:\n")
print(app.isnull().sum())

print("\nTask 11 Completed Successfully!")
