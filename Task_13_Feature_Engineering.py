# ============================================================
# Task 13 : Feature Engineering
# Credit Card Approval Prediction System
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# Read Datasets
# ------------------------------------------------------------

application_df = pd.read_csv("Dataset/application_record.csv")
credit_df = pd.read_csv("Dataset/credit_record.csv")

# ------------------------------------------------------------
# Remove Duplicates
# ------------------------------------------------------------

application_df.drop_duplicates(inplace=True)
credit_df.drop_duplicates(inplace=True)

# ------------------------------------------------------------
# Handle Missing Values
# ------------------------------------------------------------

for col in application_df.select_dtypes(include=['object']).columns:
    application_df[col].fillna(application_df[col].mode()[0], inplace=True)

for col in application_df.select_dtypes(include=['int64','float64']).columns:
    application_df[col].fillna(application_df[col].median(), inplace=True)

# ------------------------------------------------------------
# Feature Engineering
# ------------------------------------------------------------

# Convert Days to Positive Values
application_df['AGE_DAYS'] = application_df['DAYS_BIRTH'].abs()
application_df['EMPLOYMENT_DAYS'] = application_df['DAYS_EMPLOYED'].abs()

# Convert Days into Years
application_df['AGE_YEARS'] = (application_df['AGE_DAYS'] / 365).astype(int)
application_df['EMPLOYMENT_YEARS'] = (application_df['EMPLOYMENT_DAYS'] / 365).astype(int)

# Income Per Family Member
application_df['INCOME_PER_MEMBER'] = (
    application_df['AMT_INCOME_TOTAL'] /
    application_df['CNT_FAM_MEMBERS']
)

# ------------------------------------------------------------
# Display Engineered Features
# ------------------------------------------------------------

print("\nEngineered Dataset")

print(application_df[
    [
        'AGE_YEARS',
        'EMPLOYMENT_YEARS',
        'INCOME_PER_MEMBER'
    ]
].head())

print("\nFeature Engineering Completed Successfully!")
