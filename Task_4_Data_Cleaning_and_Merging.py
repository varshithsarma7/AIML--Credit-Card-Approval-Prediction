# ============================================================
# Task 4 : Data Cleaning and Merging
# Credit Card Approval Prediction System
# ============================================================

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

# Fill categorical columns with mode
for col in application_df.select_dtypes(include="object").columns:
    application_df[col].fillna(application_df[col].mode()[0], inplace=True)

# Fill numerical columns with median
for col in application_df.select_dtypes(include=["int64","float64"]).columns:
    application_df[col].fillna(application_df[col].median(), inplace=True)

# ------------------------------------------------------------
# Merge Datasets using ID
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

print("\nMerged Dataset Preview:")
print(merged_df.head())

print("\nMerged Dataset Information:")
merged_df.info()

print("\nTask 4 Completed Successfully!")
