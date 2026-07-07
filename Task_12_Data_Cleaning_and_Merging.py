# ============================================================
# Task 12 : Data Cleaning and Merging
# Credit Card Approval Prediction System
# ============================================================

# Import Library
import pandas as pd

# ------------------------------------------------------------
# Read Datasets
# ------------------------------------------------------------

application_df = pd.read_csv("Dataset/application_record.csv")
credit_df = pd.read_csv("Dataset/credit_record.csv")

# ------------------------------------------------------------
# Remove Duplicate Records
# ------------------------------------------------------------

application_df = application_df.drop_duplicates()
credit_df = credit_df.drop_duplicates()

# ------------------------------------------------------------
# Handle Missing Values
# ------------------------------------------------------------

# Fill numerical columns with median
for col in application_df.select_dtypes(include=['int64', 'float64']).columns:
    application_df[col].fillna(application_df[col].median(), inplace=True)

# Fill categorical columns with mode
for col in application_df.select_dtypes(include=['object']).columns:
    application_df[col].fillna(application_df[col].mode()[0], inplace=True)

# ------------------------------------------------------------
# Merge Datasets Using ID
# ------------------------------------------------------------

merged_df = pd.merge(
    application_df,
    credit_df,
    on="ID",
    how="inner"
)

# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------

print("\nMerged Dataset Shape:")
print(merged_df.shape)

print("\nFirst Five Rows:")
print(merged_df.head())

print("\nDataset Information:")
merged_df.info()

print("\nMissing Values After Merging:")
print(merged_df.isnull().sum())

print("\nTask 12 Completed Successfully!")
