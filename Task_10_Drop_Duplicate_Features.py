# ============================================================
# Task 10 : Drop Duplicate Features
# Credit Card Approval Prediction System
# ============================================================

# Import Library
import pandas as pd

# ------------------------------------------------------------
# Read Dataset
# ------------------------------------------------------------

app = pd.read_csv("Dataset/application_record.csv")

# ------------------------------------------------------------
# Dataset Shape Before Removing Duplicates
# ------------------------------------------------------------

print("\nDataset Shape Before Removing Duplicates:")
print(app.shape)

# ------------------------------------------------------------
# Count Duplicate Records
# ------------------------------------------------------------

duplicate_count = app.duplicated().sum()

print("\nNumber of Duplicate Records:")
print(duplicate_count)

# ------------------------------------------------------------
# Remove Duplicate Records
# ------------------------------------------------------------

app = app.drop_duplicates()

# ------------------------------------------------------------
# Dataset Shape After Removing Duplicates
# ------------------------------------------------------------

print("\nDataset Shape After Removing Duplicates:")
print(app.shape)

# ------------------------------------------------------------
# Verify Duplicate Records
# ------------------------------------------------------------

print("\nRemaining Duplicate Records:")
print(app.duplicated().sum())

print("\nTask 10 Completed Successfully!")
