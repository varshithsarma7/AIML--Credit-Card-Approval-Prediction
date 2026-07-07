# ============================================================
# Task 3 : Handling Missing Values
# Credit Card Approval Prediction System
# ============================================================

# Import required libraries
import pandas as pd

# Read datasets
application_df = pd.read_csv("Dataset/application_record.csv")
credit_df = pd.read_csv("Dataset/credit_record.csv")

# ------------------------------------------------------------
# Check Missing Values
# ------------------------------------------------------------

print("\nMissing Values in Application Dataset")
print(application_df.isnull().sum())

print("\nMissing Values in Credit Dataset")
print(credit_df.isnull().sum())

# ------------------------------------------------------------
# Fill Missing Values
# ------------------------------------------------------------

# Fill categorical missing values with Mode
for column in application_df.select_dtypes(include=['object']).columns:
    application_df[column].fillna(application_df[column].mode()[0], inplace=True)

# Fill numerical missing values with Median
for column in application_df.select_dtypes(include=['int64', 'float64']).columns:
    application_df[column].fillna(application_df[column].median(), inplace=True)

# Fill missing values in credit dataset (if any)
for column in credit_df.select_dtypes(include=['object']).columns:
    credit_df[column].fillna(credit_df[column].mode()[0], inplace=True)

for column in credit_df.select_dtypes(include=['int64', 'float64']).columns:
    credit_df[column].fillna(credit_df[column].median(), inplace=True)

# ------------------------------------------------------------
# Verify Missing Values
# ------------------------------------------------------------

print("\nMissing Values After Cleaning (Application Dataset)")
print(application_df.isnull().sum())

print("\nMissing Values After Cleaning (Credit Dataset)")
print(credit_df.isnull().sum())

print("\nTask 3 Completed Successfully!")
