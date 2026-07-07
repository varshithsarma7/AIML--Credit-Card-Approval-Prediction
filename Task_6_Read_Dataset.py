# ============================================================
# Task 6 : Read the Dataset
# Credit Card Approval Prediction System
# ============================================================

# Import Libraries
import pandas as pd

# ------------------------------------------------------------
# Load the Datasets
# ------------------------------------------------------------

application_df = pd.read_csv("Dataset/application_record.csv")
credit_df = pd.read_csv("Dataset/credit_record.csv")

# ------------------------------------------------------------
# Display First Five Records
# ------------------------------------------------------------

print("\n========== APPLICATION DATASET ==========")
print(application_df.head())

print("\n========== CREDIT RECORD DATASET ==========")
print(credit_df.head())

# ------------------------------------------------------------
# Display Dataset Shape
# ------------------------------------------------------------

print("\nApplication Dataset Shape :", application_df.shape)
print("Credit Record Dataset Shape :", credit_df.shape)

# ------------------------------------------------------------
# Display Dataset Information
# ------------------------------------------------------------

print("\n========== APPLICATION DATASET INFO ==========")
application_df.info()

print("\n========== CREDIT RECORD DATASET INFO ==========")
credit_df.info()

# ------------------------------------------------------------
# Display Column Names
# ------------------------------------------------------------

print("\nApplication Dataset Columns")
print(application_df.columns.tolist())

print("\nCredit Record Dataset Columns")
print(credit_df.columns.tolist())

# ------------------------------------------------------------
# Display Data Types
# ------------------------------------------------------------

print("\nApplication Dataset Data Types")
print(application_df.dtypes)

print("\nCredit Record Dataset Data Types")
print(credit_df.dtypes)

print("\nTask 6 Completed Successfully!")
